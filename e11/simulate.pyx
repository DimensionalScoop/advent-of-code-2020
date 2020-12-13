# cython infer_types=True
# cython boundscheck=False
# cython wraparound=False
cimport cython
cimport numpy as np
import numpy as np
import numpy.testing as npt
#from main import EMPTY, OCCUPIED, FLOOR

ctypedef np.uint8_t bol

cdef bol EMPTY = 0
cdef bol OCCUPIED = 1
cdef bol FLOOR = 2

# cdef int sum2d(bol[:, ::1] arr) nogil:
#     cdef size_t i, j, I, J
#     cdef int total = 0
#     I = arr.shape[0]
#     J = arr.shape[1]
#     for i in range(I):
#         for j in range(J):
#             total += arr[i, j]
#     return total

def neighbors(seats, x, y):
    assert x > 0 and y > 0, "neighbors do not exist"
    assert x < seats.shape[0] - 1, "neighbors do not exist"
    assert y < seats.shape[1] - 1, "neighbors do not exist"

    # the seat at (x,y) and all adjecent seats
    seats = np.asarray(seats,dtype=np.uint8)
    block = seats[x - 1 : x + 2, y - 1 : y + 2]
    assert block.shape == (3, 3), "neighbors do not exist"
    cdef int n = np.sum(block == OCCUPIED)
    if seats[x, y] == OCCUPIED:
        n -= 1

    assert 0 <= n <= 8, "too many or to few neighbors ("+str(n)+")"
    return n

cdef int fast_neighbors(bol[:,::1] map, int x, int y) nogil:
    #assert x > 0 and y > 0, "neighbors do not exist"
    #assert x < map.shape[0] - 1, "neighbors do not exist"
    #assert y < map.shape[1] - 1, "neighbors do not exist"

    cdef int i,k
    cdef int n = 0

    for i in range(x-1,x+2):
        for k in range(y-1,y+2):
            if i==x and k==y:
                continue
            if map[i,k] == OCCUPIED:
                n += 1
            
    #assert 0 <= n <= 8, "too many or to few neighbors ("+str(n)+")"
    return n

cdef int[8][2] directions = [
        (1, 0),  # cardinal
        (0, 1),
        (-1, 0),
        (0, -1),
        (-1, -1),  # diagonal
        (1, 1),
        (-1, 1),
        (1, -1),
    ]

cpdef int visual_neighbors(bol[:,:] map, int x, int y):    
    cdef int n = 0
    cdef int i
    cdef int eye_x
    cdef int eye_y
    cdef bol content

    for i in range(8):
        eye_x = x
        eye_y = y
        while True:
            eye_x += directions[i][0]
            eye_y += directions[i][1]

            if is_out_of_bounds(eye_x,eye_y, map):
                # if we reach the end of the array and touch no seats,
                # there's no neighbor, so n+=0
                break
            content = map[eye_x,eye_y]
            if content == FLOOR:
                continue
            elif content == EMPTY:
                break
            elif content == OCCUPIED:
                n += 1
                break
            else:
                raise NotImplementedError(content)

    assert 0 <= n <= 8, "too many or to few neighbors"
    return n


cdef bol is_out_of_bounds(int x, int y, bol[:,:] array):
    # we need to disallow wrap-around
    if x < 0 or x >= array.shape[0]:
        return True
    if y < 0 or y >= array.shape[1]:
        return True
    return False

cpdef step(map_np, bol adjacent=True):
    new_map_np = np.ones_like(map_np) * FLOOR

    cdef bol[:,::1] new_map = new_map_np
    cdef bol [:,::1] map = map_np
    cdef int len_x = map.shape[0], len_y = map.shape[1]
    cdef int n,x,y,too_many_people

    if adjacent:
        too_many_people = 4
    else:
        too_many_people = 5

    # respect the padding
    for x in range(1, len_x - 1):
        for y in range(1, len_y - 1):
            if map[x, y] == FLOOR:
                new_map[x, y] = FLOOR
            else:
                if adjacent:
                    n = fast_neighbors(map, x, y)
                else:
                    n = visual_neighbors(map, x, y)

                if map[x, y] == EMPTY and n == 0:
                    new_map[x, y] = OCCUPIED
                elif map[x, y] == OCCUPIED and n >= too_many_people:
                    new_map[x, y] = EMPTY
                else:
                    new_map[x, y] = map[x, y]

    return new_map_np
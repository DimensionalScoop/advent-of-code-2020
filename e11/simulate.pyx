# cython infer_types=True
cimport cython
cimport numpy as np
import numpy as np
import numpy.testing as npt

raise Exception("Out of date, simulate_python.py is newer")

ctypedef np.uint8_t bol

cdef bol EMPTY= 0
cdef bol OCCUPIED=1

cdef int sum2d(bol[:, ::1] arr) nogil:
    cdef size_t i, j, I, J
    cdef int total = 0
    I = arr.shape[0]
    J = arr.shape[1]
    for i in range(I):
        for j in range(J):
                total += arr[i, j]
    return total


cdef int neighbors(bol[:,::1] seats, int x, int y) nogil:
    return sum2d(seats[x - 1 : x + 2, y - 1 : y + 2]) - seats[x, y]

cdef int visual_neighbors(bol[:,::1] map, int x, int y):
    # get all seats in each direction
    cardinals = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    diagonals = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
    cdef int n = 0
    cdef int[2] d
    cdef int[2] eye

    for d in np.array(cardinals + diagonals):
        eye = (x,y)
        while True:
            eye += d
            if is_out_of_bounds(eye, map):
                # if we reach the end of the array and touch no seats,
                # there's no neighbor, so n+=0
                break
            if map[eye[0],eye[1]] == FLOOR:
                continue
            if map[eye[0],eye[1]] == EMPTY:
                n += 0
                break
            if map[eye[0],eye[1]] == OCCUPIED:
                n += 1
                break

    return n


cdef bol is_out_of_bounds(int[2] index, bol[:,::1] array):
    cdef int i
    for i in range(len(index)):
        if index[i] < 0 or index[i] >= array.shape[i]:
            return True
    return False


def step(bol[:,::1] seats, bol[:,::1] floor, bol adjecent):
    new_seats_np = np.zeros_like(seats, dtype=np.uint8)
    cdef bol[:,:] new_seats = new_seats_np
    cdef Py_ssize_t len_x = seats.shape[0]
    cdef Py_ssize_t len_y = seats.shape[1]
    cdef Py_ssize_t x,y

    cdef bol[:,:] map
    cdef int too_many_people 
    if adjacent:
        map = seats
        too_many_people=4
    else:
        map = seats.copy()
        map[floor] = FLOOR
        too_many_people=5

    for x in range(1, len_x-1):
        for y in range(1, len_y-1):
            if floor[x, y]:
                new_seats[x, y] = EMPTY
            else:
                n = neighbors(seats, x, y)

                if seats[x, y] == EMPTY and n == 0:
                    new_seats[x, y] = OCCUPIED
                elif seats[x, y] == OCCUPIED and n >= 4:
                    new_seats[x, y] = EMPTY
                else:
                    new_seats[x, y] = seats[x, y]

    return new_seats_np
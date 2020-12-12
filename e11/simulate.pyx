cimport cython
cimport numpy as np
import numpy as np
import numpy.testing as npt

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

def step(bol[:,::1] seats, bol[:,::1] floor):
    new_seats_np = np.zeros_like(seats, dtype=np.uint8)
    cdef bol[:,:] new_seats = new_seats_np
    cdef Py_ssize_t len_x = seats.shape[0]
    cdef Py_ssize_t len_y = seats.shape[1]
    cdef Py_ssize_t x,y

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
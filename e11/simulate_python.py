import numpy as np
import numpy.testing as npt

EMPTY, OCCUPIED = False, True

def neighbors(seats, x, y):
    return np.sum(seats[x - 1 : x + 2, y - 1 : y + 2]) - seats[x, y]


def step(seats, floor):
    new_seats = np.zeros_like(seats, dtype=np.uint8)
    len_x, len_y = seats.shape[0], seats.shape[1]  # -1 is the padding

    for x in range(1, len_x):
        for y in range(1, len_y):
            if floor[x, y]:
                new_seats[x, y] = EMPTY
            else:
                n = neighbors(seats, x, y)
                assert 0 <= n <= 8

                if seats[x, y] == EMPTY and n == 0:
                    new_seats[x, y] = OCCUPIED
                elif seats[x, y] == OCCUPIED and n >= 4:
                    new_seats[x, y] = EMPTY
                else:
                    new_seats[x, y] = seats[x, y]

    #npt.assert_equal(new_seats[floor], EMPTY)

    return new_seats
import numpy as np
import numpy.testing as npt

EMPTY, OCCUPIED = 0, 1
FLOOR = 2


def neighbors(seats, x, y):
    return np.sum(seats[x - 1 : x + 2, y - 1 : y + 2]) - seats[x, y]


def visual_neighbors(map, x, y):
    # get all seats in each direction
    cardinals = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    diagonals = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
    n = 0

    for d in np.array(cardinals + diagonals):
        eye = np.array((x, y))
        while True:
            eye += d
            if is_out_of_bounds(eye, map):
                # if we reach the end of the array and touch no seats,
                # there's no neighbor, so n+=0
                break
            if map[tuple(eye)] == FLOOR:
                continue
            if map[tuple(eye)] == EMPTY:
                n += 0
                break
            if map[tuple(eye)] == OCCUPIED:
                n += 1
                break

    return n


def is_out_of_bounds(index, array):
    # we need to disallow wrap-around
    for i in range(len(index)):
        if index[i] < 0 or index[i] >= array.shape[i]:
            return True
    return False


def step(seats, floor, adjacent=True):
    new_seats = np.zeros_like(seats, dtype=np.uint8)
    floor = np.asarray(floor,dtype=np.bool)
    len_x, len_y = seats.shape[0], seats.shape[1]

    if adjacent:
        map = seats
        too_many_people = 4
    else:
        map = seats.copy()
        map[floor] = FLOOR
        too_many_people = 5

    for x in range(0, len_x):
        for y in range(0, len_y):
            if floor[x, y]:
                new_seats[x, y] = EMPTY
            else:
                if adjacent:
                    n = neighbors(map, x, y)
                else:
                    n = visual_neighbors(map, x, y)
                assert 0 <= n <= 8

                if seats[x, y] == EMPTY and n == 0:
                    new_seats[x, y] = OCCUPIED
                elif seats[x, y] == OCCUPIED and n >= too_many_people:
                    new_seats[x, y] = EMPTY
                else:
                    new_seats[x, y] = seats[x, y]

    npt.assert_equal(new_seats[floor==True], EMPTY)

    return new_seats
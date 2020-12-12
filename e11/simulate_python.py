import numpy as np
import numpy.testing as npt
from main import EMPTY, OCCUPIED, FLOOR


def neighbors(seats, x, y):
    assert x > 0 and y > 0
    assert x < seats.shape[0] - 1
    assert y < seats.shape[1] - 1

    # the seat at (x,y) and all adjecent seats
    block = seats[x - 1 : x + 2, y - 1 : y + 2]
    assert block.shape == (3, 3)
    n = np.count_nonzero(block == OCCUPIED)
    if seats[x, y] == OCCUPIED:
        n -= 1

    assert 0 <= n <= 8
    return n


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

    assert 0 <= n <= 8
    return n


def is_out_of_bounds(index, array):
    # we need to disallow wrap-around
    for i in range(len(index)):
        if index[i] < 0 or index[i] >= array.shape[i]:
            return True
    return False


def step(map, adjacent=True):
    new_map = np.ones_like(map) * FLOOR
    len_x, len_y = map.shape[0], map.shape[1]

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
                    n = neighbors(map, x, y)
                else:
                    n = visual_neighbors(map, x, y)

                if map[x, y] == EMPTY and n == 0:
                    new_map[x, y] = OCCUPIED
                elif map[x, y] == OCCUPIED and n >= too_many_people:
                    new_map[x, y] = EMPTY
                else:
                    new_map[x, y] = map[x, y]

    return new_map
import numpy as np
import numpy.testing as npt
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

EMPTY, OCCUPIED = False, True
char_to_seat = {"L": EMPTY, "#": OCCUPIED, ".": EMPTY}
char_to_floor = {"L": False, "#": False, ".": True}
file = open("e11/input").readlines()
floor = [[char_to_floor[c] for c in l.strip("\n")] for l in file]
seats = [[char_to_seat[c] for c in l.strip("\n")] for l in file]
floor = np.pad(floor, 1, "constant", constant_values=(1))
seats = np.pad(seats, 1, "constant", constant_values=(0))


def neighbors(x, y):
    return np.sum(seats[x - 1 : x + 2, y - 1 : y + 2]) - seats[x, y]


def step(seats, floor):
    new_seats = np.zeros_like(seats)
    len_x, len_y = seats.shape[0], seats.shape[1]  # -1 is the padding

    for x in range(1, len_x):
        for y in range(1, len_y):
            if floor[x, y]:
                new_seats[x, y] = EMPTY
            else:
                n = neighbors(x, y)
                assert 0 <= n <= 8

                if seats[x, y] == EMPTY and n == 0:
                    new_seats[x, y] = OCCUPIED
                elif seats[x, y] == OCCUPIED and n >= 4:
                    new_seats[x, y] = EMPTY
                else:
                    new_seats[x, y] = seats[x, y]

    npt.assert_equal(new_seats[floor], EMPTY)

    return new_seats


plot_steps = True
count_steps = 0
previous_seats = None
while not np.array_equal(seats, previous_seats):
    if plot_steps:
        show = seats.copy()
        show[floor] = -1
        plt.imshow(show, cmap="Accent", vmin=-1, vmax=1)
        plt.colorbar()
        plt.savefig("e11/plt/" + str(count_steps) + ".png")
        plt.clf()

    previous_seats = seats
    seats = step(seats, floor)
    count_steps += 1
yyy
print("took", count_steps, "steps")
print(np.sum(seats))
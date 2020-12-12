import numpy as np
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

floor = np.asarray(floor,dtype=np.uint8)
seats = np.asarray(seats,dtype=np.uint8)

from simulate import step

plot_steps = False
count_steps = 0
previous_seats = None
while not np.array_equal(seats, previous_seats):
    print(count_steps,end=" ")
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

print("took", count_steps, "steps")
print(np.sum(seats))
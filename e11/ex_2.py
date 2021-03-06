import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
from main import EMPTY,OCCUPIED,FLOOR
from main import get_map,converters
from simulate import step

def doit(print_=True):
    map = get_map("input",FLOOR)

    plot_steps = False
    count_steps = 0
    previous_map = None
    while not np.array_equal(map, previous_map):
        #print(count_steps,end=" ")
        if plot_steps:
            plt.imshow(map, cmap="Accent", vmin=EMPTY, vmax=FLOOR)
            plt.colorbar()
            plt.savefig("e11/plt/" + str(count_steps) + ".png")
            plt.clf()

        previous_map = map.copy()
        map = step(map,False)
        count_steps += 1

    if print_:
        print("took", count_steps, "steps")
        print(np.sum(map==OCCUPIED))

if __name__ == "__main__":
    doit(True)
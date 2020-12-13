import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
from main import EMPTY,OCCUPIED,FLOOR
from main import get_map,converters,draw_map
from simulate import step

def doit(print_=True):
    map = get_map("input",FLOOR)

    plot_steps = False
    count_steps = 0
    previous_map = None
    while not np.array_equal(map, previous_map):
        #print(count_steps,end=" ")
        if plot_steps:
            draw_map(map,str(count_steps),False)

        previous_map = map.copy()
        map = step(map)
        count_steps += 1

    if print_:
        print("took", count_steps, "steps")
        print(np.sum(map==OCCUPIED))

if __name__ == "__main__":
    doit(True)
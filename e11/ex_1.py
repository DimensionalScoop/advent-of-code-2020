import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
from main import EMPTY,OCCUPIED,FLOOR
from main import get_map,converters,draw_map
from simulate_python import step

map = get_map("input",FLOOR)

plot_steps = True
count_steps = 0
previous_map = None
while not np.array_equal(map, previous_map):
    print(count_steps,end=" ")
    if plot_steps:
        draw_map(map,str(count_steps),False)

    previous_map = map
    map = step(map)
    count_steps += 1

print("took", count_steps, "steps")
print(np.sum(map==OCCUPIED))
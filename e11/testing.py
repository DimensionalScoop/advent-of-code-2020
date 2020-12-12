import numpy as np
from simulate_python import visual_neighbors

EMPTY, OCCUPIED, FLOOR = 0,1,2
char_to_seat = {"L": EMPTY, "#": OCCUPIED, ".": FLOOR}

def get_map(name):
    file = open("e11/"+name).readlines()
    map = [[char_to_seat[c] for c in l.strip("\n")] for l in file]
    map = np.pad(map, 1, "constant", constant_values=(FLOOR))
    return map

map = get_map("test-1")
pos = (5,4)
assert map[pos] == EMPTY
n= visual_neighbors(map,*pos)
assert n == 8

map = get_map("test-2")
pos = (2,2)
assert map[pos] == EMPTY
n= visual_neighbors(map,*pos)
assert n == 0

map = get_map("test-3")
pos = (4,4)
assert map[pos] == EMPTY
n= visual_neighbors(map,*pos)
assert n == 0
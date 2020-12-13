import numpy as np
import numpy.testing as npt
from simulate_python import neighbors, visual_neighbors, step
import simulate as c_sim
from main import EMPTY, OCCUPIED, FLOOR
from main import get_map, converters, draw_map

map = get_map("test-1", FLOOR)
pos = (5, 4)
assert map[pos] == EMPTY
n = visual_neighbors(map, *pos)
assert n == 8

c_n = c_sim.visual_neighbors(map, *pos)
assert c_n == n

c_n = c_sim.neighbors(map,*pos)
n = neighbors(map,*pos)
assert c_n==n


map = get_map("test-2", FLOOR)
pos = (2, 2)
assert map[pos] == EMPTY
n = visual_neighbors(map, *pos)
assert n == 0

pos = (2, 4)
assert map[pos] == EMPTY
n = visual_neighbors(map, *pos)
assert n == 1

c_n = c_sim.visual_neighbors(map, *pos)
assert c_n == n


map = get_map("test-3", FLOOR)
pos = (4, 4)
assert map[pos] == EMPTY
n = visual_neighbors(map, *pos)
assert n == 0

c_n = c_sim.visual_neighbors(map, *pos)
assert c_n == n

# step-by-step test
files = ["test-sim/" + str(i) for i in range(7)]
maps = [get_map(f, FLOOR) for f in files]
last_map = None
for i in range(len(maps) - 1):
    this_map = maps[i]
    next_map = maps[i + 1]

    copy = this_map.copy()
    calc_map = step(this_map, False)
    npt.assert_array_equal(copy, this_map)
    npt.assert_array_equal(next_map, calc_map)

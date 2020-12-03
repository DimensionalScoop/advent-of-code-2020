import numpy as np
import matplotlib.pyplot as plt

with open("3/input") as f:
    lines = [l.strip("\n") for l in f.readlines()]

map = []
for l in lines:
    map.append(list(0 if c == "." else 1 for c in l))
map = np.asarray(map).T  # 0 is left-right, 1 is up-down
assert map.shape[1] > map.shape[0]  # map should be tall and slim

velocities = np.asarray([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])
trees_by_vs = []

for v in velocities:
    sledge_position = np.array((0, 0))
    count_steps = int(map.shape[1] / v[1])
    trees = 0
    for step in range(count_steps):
        trees += map[sledge_position[0], sledge_position[1]]
        sledge_position += v
        sledge_position[0] = sledge_position[0] % map.shape[0]
    trees_by_vs.append(trees)

print(np.prod(trees_by_vs))
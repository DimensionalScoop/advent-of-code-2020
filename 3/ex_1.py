import numpy as np
import matplotlib.pyplot as plt

with open("3/input") as f:
    lines = [l.strip("\n") for l in f.readlines()]

map = []
for l in lines:
    map.append(list(0 if c == "." else 1 for c in l))
map = np.asarray(map).T  # 0 is left-right, 1 is up-down
assert map.shape[1] > map.shape[0]  # map should be tall and slim

velocity = np.array((3, 1))
sledge_position = np.array((0, 0))
count_steps = int(map.shape[1] / velocity[1])
trees = 0
for step in range(count_steps):
    trees += map[sledge_position[0], sledge_position[1]]
    sledge_position += velocity
    sledge_position[0] = sledge_position[0] % map.shape[0]


def plot_trajectory():
    count_tiles = int(np.ceil(velocity[0] * count_steps / map.shape[0]))
    plt.imshow(np.tile(map, [count_tiles, 1]).T, aspect="equal")
    plt.arrow(0, 0, *(velocity * count_steps), label="Toboggan")
    plt.colorbar(label="Tree Density")
    plt.legend()
    plt.show()

print(trees)
plot_trajectory()
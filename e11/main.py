import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

EMPTY, OCCUPIED, FLOOR = 0, 1, 2


class converters:
    full = {"L": EMPTY, "#": OCCUPIED, ".": FLOOR}
    is_occupied = {"L": EMPTY, "#": OCCUPIED, ".": EMPTY}
    is_floor = {"L": False, "#": False, ".": True}


def get_map(name, pad_with=None, converter=converters.full):
    file = open("e11/" + name).readlines()
    map = [[converter[c] for c in l.strip("\n")] for l in file]
    if pad_with is not None:
        map = np.pad(map, 1, "constant", constant_values=(pad_with))
    return np.asarray(map, dtype=np.uint8)

def draw_map(map,save_name=None,show=True):
    plt.imshow(map, cmap="Accent", vmin=EMPTY, vmax=FLOOR)
    plt.colorbar()
    if save_name is not None:
        plt.savefig("e11/plt/" + str(save_name) + ".png")
    if show:
        plt.show()
    plt.clf()
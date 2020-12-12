import numpy as np
import numpy.testing as npt

guidance = [(l[0], int(l[1:])) for l in open("e12/input").readlines()]

compass_to_dir = {
    "N": np.array((0, -1)),
    "S": np.array((0, 1)),
    "E": np.array((-1, 0)),
    "W": np.array((1, 0)),
}


def vec_rot(vector, angle):
    angle = np.deg2rad(angle)
    l = np.sqrt(vector[0] ** 2 + vector[1] ** 2)
    w = np.arctan2(vector[1], vector[0])
    return np.array([np.cos(w + angle), np.sin(w + angle)]) * l


npt.assert_array_equal(compass_to_dir["W"], vec_rot(compass_to_dir["N"], 90))

position = np.array((0.0, 0.0))
waypoint_relative = np.array((-10.0, -1.0))

for move, value in guidance:
    if move == "F":
        position += waypoint_relative * value
    elif move == "L":
        waypoint_relative = vec_rot(waypoint_relative, value)
    elif move == "R":
        waypoint_relative = vec_rot(waypoint_relative, -value)
    else:
        waypoint_relative += compass_to_dir[move] * value
print(np.round(np.sum(np.abs(position))))
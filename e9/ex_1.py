import numpy as np

sequence = np.loadtxt("e9/input", dtype=int)
lookback = 25

for i in range(lookback, len(sequence)):
    preambel = sequence[i - lookback : i]
    assert len(preambel) == lookback
    number = sequence[i]

    mat = np.tile(preambel, (lookback, 1))
    additions = mat + mat.T
    np.fill_diagonal(additions, -100)  # we should combine two different numbers

    # we do everything twice with these matrices
    num_valid = np.sum(additions == number) >= 2
    if not num_valid:
        break

print(number, "(on", i, "th line) is invalid")

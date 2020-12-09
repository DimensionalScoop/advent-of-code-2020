import numpy as np

from ex_1 import number, sequence, i

target = number
start = 0
stop = 2

while True:
    assert stop >= start + 2

    sum = sequence[start:stop].sum()

    if sum == target:
        break
    elif sum < target:
        stop += 1
    elif sum > target:
        if stop - start > 2:  # we need at least two numbers
            start += 1
        else:
            start += 1
            stop += 1

    if stop > len(sequence):
        raise Exception("Sequence not found")

cont_set = sequence[start:stop]
weakness = cont_set.min() + cont_set.max()
print(weakness)
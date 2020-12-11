import numpy as np
from scipy.special import factorial
import matplotlib.pyplot as plt

adapters = [int(i) for i in open("e10/input").readlines()]
chain = np.array([0] + sorted(adapters) + [max(adapters) + 3])

continous_one_series = []
current_set_size = 0
for i in range(1, len(chain)):
    diff = chain[i] - chain[i - 1]
    if diff != 1:
        if current_set_size != 0:
            continous_one_series.append(current_set_size)
            current_set_size = 0
    elif diff == 1:
        current_set_size += 1
if current_set_size != 0:
    continous_one_series.append(current_set_size)
    current_set_size = 0

# counted possible combinations for each difference by hand
comb_by_diff = {1:1,2:2,3:4,4:7}
single_combinations = [comb_by_diff[i] for i in continous_one_series]
total_combinations = np.prod(single_combinations)
print(total_combinations)
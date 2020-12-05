import matplotlib.pyplot as plt
import numpy as np
from ex_1 import parse_code

passes = open("e5/input").readlines()
passes = np.array([parse_code(p) for p in passes])

sort_by_id = np.argsort(passes[:,2])
sorted_passes = passes[sort_by_id,:]
shift_diff = sorted_passes[:-1,2] - sorted_passes[1:,2]
hole = np.argmin(shift_diff)

print(
    sorted_passes[hole],
    sorted_passes[hole+1]
    )

# for r,c,id in passes:   
#     plt.plot(c,r,'rs')
# plt.show()
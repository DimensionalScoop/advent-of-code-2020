import numpy as np
import sympy as s
from sympy.matrices.dense import matrix_multiply_elementwise
from data import buses

schedule = np.array(list([(t, b) for t, b in enumerate(buses) if b != -1]))
count_buses = schedule.shape[0]
delays = schedule[
    :, 0
]  # time after which the bus should leave, realtive to the first bus
periods = schedule[:, 1]  # bus returns ever nth minutes to the airport

departure = 0
increment = periods[0]
for i in range(1, count_buses):
    while True:
        # does this bus leave at the right time?
        if (departure + delays[i]) % periods[i] == 0:
            # make sure that all further time steps
            # can't make this bus miss it's time slot
            increment *= periods[i]
            break
        departure += increment

for d, p in zip(delays, periods):
    assert (departure + d) % p == 0

print(departure)
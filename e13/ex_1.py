import numpy as np
from data import buses

now = 1006726
buses = [b for b in buses if b!=-1]


def find_bus():
    departure = now
    while True:
        for b in buses:
            if departure % b == 0:
                return b, departure
        departure += 1

id, earlies_departure = find_bus()
print(id*(earlies_departure-now))
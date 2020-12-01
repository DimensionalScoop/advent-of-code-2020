#%%
import numpy as np
import numpy.testing as npt

target = 2020
# %%
numbers = np.loadtxt("1/input")
# %%
def find_sum():
    for i,a in enumerate(numbers):
        for j,b in enumerate(numbers):
            for k,c in enumerate(numbers):
                if a+b+c == target:
                    return i,j,k

i,j,k = find_sum()
npt.assert_almost_equal(numbers[i]+numbers[j]+numbers[k],target)
print(numbers[i]*numbers[j]*numbers[k])

import numpy as np

target = 2020
numbers = np.loadtxt("1/input")

# generate a matrix that consists of repeated number vectors
number_matrix = np.tile(numbers, (len(numbers), 1))
# we actually only need a triangular matrix, but we are trying to keep it simple
# so we're doing every addition twice
add_matrix = number_matrix + number_matrix.T

# we find two entries, only use one of those
indices_of_desired_entries = np.where(add_matrix == target)[0]

a, b = indices_of_desired_entries
print(numbers[a], "+", numbers[b], "=", numbers[a] + numbers[b])
print(numbers[a], "*", numbers[b], "=", numbers[a] * numbers[b])

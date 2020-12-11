import numpy as np

adapters = [int(i) for i in open("e10/input").readlines()]
chain = np.array([0] + sorted(adapters) + [max(adapters) + 3])
diffs = chain[1:] - chain[:-1]
diff_count = dict(zip(*np.unique(diffs,return_counts=True)))
print(diff_count[1]*diff_count[3])
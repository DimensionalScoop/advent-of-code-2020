from plumbum import local
import re
from os import listdir
from os.path import isfile, join
import pandas as pd
import matplotlib.pyplot as plt

count_lines = local["cloc"]

path = "."
code_dirs = [
    f for f in listdir(path) if not isfile(join(path, f)) and not f.startswith(".")
]
code_dirs = sorted(code_dirs)

df = pd.DataFrame()
pattern = r"Python\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)"
for dir in code_dirs:
    day = dir[1:]
    data = re.findall(pattern, count_lines(dir))[0]
    df = df.append(
        {
            "day": int(day),
            "files": int(data[0]),
            "blank lines": int(data[1]),
            "comments": int(data[2]),
            "code lines": int(data[3]),
        }, ignore_index=True
    )

df["comments density"] = 100*df["comments"] / df["code lines"]

df.plot(x='day')
plt.title("Advent of Code Statistics")
plt.show()
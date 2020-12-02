import regex as re
import pandas as pd

table = pd.read_csv("2/input",sep=": ", names=["policy","password"])


def is_valid(password, policy):
    r = re.search("(\d+)-(\d+) (\w)", policy)
    count_min, count_max, letter = r.groups()
    count_actual = password.count(letter)
    return int(count_min) <= count_actual <= int(count_max)

assert not is_valid("1iodjoi321jd9i1e","2-5 g")
assert is_valid("1iodjoi3gg21jd9i1e","2-5 g")
assert is_valid("1iodjoigggg321jd9i1e","2-5 g")
assert is_valid("ggggg","2-5 g")
assert not is_valid("1iodjoi321jdgggggggg9i1e","2-5 g")


table["is_valid"] = table.apply(lambda c: is_valid(c['password'],c['policy']), axis=1)

print("Valid passwords:",table["is_valid"].sum())
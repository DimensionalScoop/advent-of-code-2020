import regex as re
import pandas as pd

table = pd.read_csv("2/input",sep=": ", names=["policy","password"])

def is_valid(password, policy):
    r = re.search("(\d+)-(\d+) (\w)", policy)
    index_a, index_b, letter = r.groups()
    try:
        a = password[int(index_a) -1] == letter
    except:
        a = False
    try:
        b = password[int(index_b) -1] == letter
    except:
        b = False
    return a != b


assert is_valid("1g3456","2-5 g")
assert is_valid("1234g6","2-5 g")
assert is_valid("1g","2-5 g")
assert not is_valid("1g34g6","2-5 g")
assert not is_valid("ggggggggggg","2-5 g")

assert is_valid("abcde", "1-3 a")
assert not is_valid("cdefg", "1-3 b")
assert not is_valid("ccccccccc","2-9 c")

assert is_valid("ttfjvvtgxtctrntnhtt","9-12 t")
assert not is_valid("kgkkkkkjf","8-9 k")


table["is_valid"] = table.apply(lambda c: is_valid(c['password'],c['policy']), axis=1)

print("Valid passwords:",table["is_valid"].sum())
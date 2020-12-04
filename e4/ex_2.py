import numpy as np
import re
from ex_1 import parse_entry, read
from ex_1 import is_valid as has_required_fields


conditions = {
    "byr": lambda y: 1920 <= int(y) <= 2002,
    "iyr": lambda y: 2010 <= int(y) <= 2020,
    "eyr": lambda y: 2020 <= int(y) <= 2030,
    "hgt": lambda h: (150 <= int(h[:-2]) <= 193)
    if h.endswith("cm")
    else (59 <= int(h[:-2]) <= 76),
    "hcl": lambda c: re.fullmatch(r"^#[0-9a-f]{6}$", c) is not None,
    "ecl": lambda s: s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda n: re.fullmatch(r"^[0-9]{9}$", n) is not None,
    "cid": lambda _: True,
}


def fields_valid(entry: dict):
    for k in entry:
        value = entry[k]
        try:
            if not conditions[k](value):
                return False
        except ValueError:
            return False
    return True


entries = [parse_entry(e) for e in read("e4/input")]
all_required_fields_exists = [has_required_fields(e) for e in entries]
all_fields_valid = [fields_valid(e) for e in entries]

print(sum(np.array(all_required_fields_exists) & np.array(all_fields_valid)))
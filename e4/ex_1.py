import numpy as np
import re


def read(filename):
    with open(filename) as f:
        file = f.readlines()

    if file[-1] != "\n":
        file.append("\n")

    entries = []
    buffer = []
    for line in file:
        if line == "\n":  # we guarantee that the file ends with a \n
            buffer = "".join(buffer).replace("\n", " ")
            entries.append(buffer)
            buffer = []
            continue
        buffer.append(line)
    return entries


def parse_entry(string):
    pattern = r"(\w+):([\w#\d]+)"
    return dict(re.findall(pattern, string))


all_fields = set(
    [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        # "cid",
    ]
)


def is_valid(entry: dict):
    fields = set(entry.keys())
    missing_fields = all_fields.difference(fields)
    return_value = len(missing_fields) == 0

    if return_value:
        assert len(fields) == 7 or len(fields) == 8
        for f in all_fields:
            assert f in fields
    else:
        assert len(fields) < 8

    return return_value

if __name__ == "__main__":
    entries = [parse_entry(e) for e in read("4/input")]
    valids = [is_valid(e) for e in entries]
    print(sum(valids))
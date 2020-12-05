import numpy as np
import numpy.testing as npt
from typing import *


def parse_code(code: str):
    row, column = seperate_row_from_column(code)
    row = code_to_bin(row, "F", "B")
    column = code_to_bin(column, "L", "R")
    return (row, column, row * 8 + column)


def seperate_row_from_column(code: str):
    first_L = code.find("L")
    first_R = code.find("R")
    if first_L == -1:
        cut_at = first_R
    elif first_R == -1:
        cut_at = first_L
    else:
        cut_at = min(first_L, first_R)
    return code[:cut_at], code[cut_at:]


def code_to_bin(code: str, zero, one):
    b = code.replace(zero, "0").replace(one, "1")
    return int(b, 2)


examples = {
    "FBFBBFFRLR": (44, 5, 357),
    "BFFFBBFRRR": (70, 7, 567),
    "FFFBBBFRRR": (14, 7, 119),
    "BBFFBBFRLL": (102, 4, 820),
}

for code in examples:
    npt.assert_allclose(parse_code(code), examples[code])

if __name__ == "__main__":
    passes = open("e5/input").readlines()
    ids = [parse_code(p)[-1] for p in passes]
    print(max(ids))
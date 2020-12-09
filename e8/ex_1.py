import re
import numpy as np

instructions = [(l[:3], int(l[4:])) for l in open("e8/input").readlines()]


def run(instructions):
    line_visited = [False] * len(instructions)
    accumulator = 0
    program_counter = 0

    while line_visited[program_counter] is False:
        line_visited[program_counter] = True
        command, value = instructions[program_counter]

        if command == "jmp":
            program_counter += value - 1  # we raise the program_counter later by 1
        elif command == "acc":
            accumulator += value
        elif command == "nop":
            pass
        else:
            raise Exception("Unknown instruction '" + command + "'")

        program_counter += 1
        if program_counter == len(instructions):
            break

    return program_counter, accumulator


if __name__ == "__main__":
    print(run(instructions)[1])
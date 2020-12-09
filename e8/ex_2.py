from ex_1 import run, instructions


def does_terminate(instructions):
    pc, acc = run(instructions)
    return pc == len(instructions)


def flip(command):
    if command == "jmp":
        return "nop"
    elif command == "nop":
        return "jmp"
    else:
        raise ValueError()


def find_new_instruction_set():
    line_visited = [False] * len(instructions)
    accumulator = 0
    program_counter = 0

    while line_visited[program_counter] is False:
        line_visited[program_counter] = True
        command, value = instructions[program_counter]

        if command == "jmp" or command == "nop":
            new_set = instructions.copy()
            new_set[program_counter] = (flip(command), value)
            if does_terminate(new_set):
                return new_set

        if command == "jmp":
            program_counter += value
            continue
        elif command == "acc":
            accumulator += value
        elif command == "nop":
            pass
        else:
            raise Exception("Unknown instruction '" + command + "'")
        program_counter += 1

        if program_counter == len(instructions):
            break


new_set = find_new_instruction_set()
print(run(new_set))
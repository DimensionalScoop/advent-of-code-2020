import itertools as it

lines = (l.strip('\n') for l in open("e6/input").readlines())
all_groups = (item for ignore, item in it.groupby(lines, lambda n: n == '') if not ignore)
yes_answers = (set.intersection(*(set(answers) for answers in group)) for group in all_groups)

count_yes = sum(len(a) for a in yes_answers)
print(count_yes)
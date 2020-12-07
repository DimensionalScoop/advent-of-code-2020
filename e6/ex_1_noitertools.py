everything = "".join(open("e6/input").readlines())
groups = [g.split('\n') for g in everything.split('\n\n')]
yes_answers = (set.union(*(set(member) for member in g)) for g in groups)

count_yes = sum(len(a) for a in yes_answers)
print(count_yes)
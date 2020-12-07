import numpy as np
from parse_input import graph

def get_containers(content):
    containers = list(graph.predecessors(content))

    if containers == []:
        return None
    else:
        c_of_containers = []
        for c in containers:
            parents = get_containers(c)
            if parents is not None:
                c_of_containers.extend(parents)
    return containers + c_of_containers

my_bag = "shiny gold"
possible_containers = np.unique(list(get_containers(my_bag)))
print(len(possible_containers))
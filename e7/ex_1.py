import re
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

lines = [l.strip("\n") for l in open("e7/input").readlines()]

graph = nx.DiGraph()


def parse_bag_rule(rule: str):
    p_valid = r"^(\w+ \w+) bags contain (?:\d+ \w+ \w+ bags?,?\s?)+."
    p_contents = r"(\d+) (\w+ \w+) bags?[(?:, ).]"

    match = re.fullmatch(p_valid, rule)
    if match is None:
        return False

    container = match.groups()[0]
    contents = re.findall(p_contents, rule)

    graph.add_node(container)
    for num, color in contents:
        graph.add_node(color)
        graph.add_edge(container, color)
    return True


def parse_empty_bag_rules(rule: str):
    pattern = r"^(\w+ \w+) bags contain no other bags.$"
    color = re.findall(pattern, rule)[0]
    assert len(list(graph.successors(color))) == 0


remaining = []
for _ in range(len(lines)):
    l = lines.pop(0)
    success = parse_bag_rule(l)
    if not success:
        remaining.append(l)

# remaining rules should be sanity checks
# do them after assembling the whole graph
for i in remaining:
    parse_empty_bag_rules(i)


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
print(possible_containers)
print(len(possible_containers))
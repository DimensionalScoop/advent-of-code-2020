import re
import networkx as nx

lines = [l.strip("\n") for l in open("e7/input").readlines()]

graph = nx.DiGraph()


def simple(r: str):
    match = re.fullmatch(r"^(\w+ \w+) bags contain (\d+) (\w+ \w+) bags*.$", r)
    if match is None:
        return False

    container, number, contents = match.groups()
    graph.add_nodes_from([container, contents])
    graph.add_edge(container, contents)
    return True


def multi(rule: str):
    p_valid = r"^(\w+ \w+) bags contain (?:\d+ \w+ \w+ bags?,?\s?)+."
    p_contents = r"(\d+) (\w+ \w+) bags?[(?:, ).]"

    match = re.fullmatch(p_valid, rule)
    if match is None:
        return False

    container = match.groups()
    contents = re.findall(p_contents, rule)

    graph.add_node(container)
    for num, color in contents:
        graph.add_node(color)
        graph.add_edge(container, color)
    return True


parsers = [multi]


def try_parse(line: str):
    for p in parsers:
        success = p(l)
        if success:
            return True
    return False


remaining = []
for _ in range(len(lines)):
    l = lines.pop(0)
    success = try_parse(l)
    if not success:
        remaining.append(l)

print(remaining[0])

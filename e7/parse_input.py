# Reads in a list of bag rules and representation these as a `graph`.
import re
import networkx as nx

graph = nx.DiGraph()

lines = [l.strip("\n") for l in open("e7/input").readlines()]


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
        graph.add_edge(container, color, bag_count=int(num))
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

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    nx.draw_kamada_kawai(graph, with_labels=True)
    plt.show()
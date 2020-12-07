from parse_input import graph

def get_contained_bags_count(container):
    total = 0
    bag_types = list(graph.successors(container))
    if bag_types == []:
        return 0
    for t in bag_types:
        bag_content = get_contained_bags_count(t)
        bag_count = graph.get_edge_data(container,t)['bag_count']
        # even if the bag is empty, we still need to count the bag itself
        total += (bag_content + 1) * bag_count
    return total


my_bag = "shiny gold"
print(get_contained_bags_count(my_bag))
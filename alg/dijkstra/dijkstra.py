# Works for directed acyclic graph，DAG with positive weight.
infinity = float("inf")

graph = {}
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

costs = {"a": 6, "b": 2, "fin": infinity}

parents = {"a": "start", "b": "start", "fin": None}

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)  # find the lowest cost node from unprocessed node.
while node is not None:  # need while loop to process all the node.
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # gets all the neighbor nodes.
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # if n node cost is smaller.
            costs[n] = new_cost  # update the cost using the smaller cost.
            parents[n] = node  # set the parent node as current node.
    processed.append(node)  # mark the node as processed.
    node = find_lowest_cost_node(costs)  # process the remaining node.

# Assert the smallest costs to get to fin is 6
assert costs["fin"] == 6

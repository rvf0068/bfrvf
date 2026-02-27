import itertools
import networkx as nx

def is_hamiltonian_cycle(graph, cycle):
    """Checks if cycle is a hamiltonian cycle in graph.
    graph is a Networkx graph, and cycle is a list of vertices"""
    n = len(set(cycle))
    if n != graph.order():
        return False
    for i in range(n-1):
        if not graph.has_edge(cycle[i], cycle[i+1]):
            return False
    if not graph.has_edge(cycle[n-1], cycle[0]):
        return False
    return True

def is_hamiltonian(graph):
    if not nx.is_connected(graph):
        return False
    vertices = list(graph.nodes())
    if len(vertices) < 3:
        return False
    perms = itertools.permutations(vertices)
    for perm in perms:
        if is_hamiltonian_cycle(graph, perm):
            return perm
    return False

def is_proper_coloring(graph, coloring):
    for edge in graph.edges():
        if coloring[edge[0]] == coloring[edge[1]]:
            return False
    return True

def is_3_colorable(graph):
    n = graph.order()
    colorings = itertools.product([0, 1, 2], repeat = n)
    for coloring in colorings:
        if is_proper_coloring(graph, coloring):
            return coloring
    return False        

def sum_of_values(values, keys):
    """Calculates the sum of values multiplied by their corresponding keys.

    Args:
        values (list): A list of numerical values.
        keys (list): A list of 0s and 1s, acting as multipliers for the values.

    Returns:
        int or float: The sum of the products of values and keys.
    """
    sum = 0
    n = len(values)
    for i in range(n):
        sum += values[i]*keys[i]
    return sum

def knapsack_problem(profits, weights, capacity, goal):
    """Solves a variation of the knapsack problem to find a sequence of items
    that meets a minimum profit goal within a given weight capacity.

    Args:
        profits (list): A list of profits for each item.
        weights (list): A list of weights for each item.
        capacity (int or float): The maximum allowable total weight.
        goal (int or float): The minimum required total profit.

    Returns:
        tuple or bool: A tuple representing the sequence of selected items (0 
        for not selected, 1 for selected) if a solution is found, otherwise 
        False.
    """
    n = len(profits)
    sequences = itertools.product([0, 1], repeat=n)
    for sequence in sequences:
        if sum_of_values(weights, sequence) <= capacity:
            if sum_of_values(profits, sequence) >= goal:
                return sequence
    return False
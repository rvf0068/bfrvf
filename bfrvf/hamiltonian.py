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
import itertools

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
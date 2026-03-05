import networkx as nx
import pytest

from bfrvf import (
    is_hamiltonian_cycle,
    is_hamiltonian,
    is_proper_coloring,
    is_3_colorable,
    sum_of_values,
    knapsack_problem,
)


# ---------------------------------------------------------------------------
# is_hamiltonian_cycle
# ---------------------------------------------------------------------------

class TestIsHamiltonianCycle:
    def test_valid_cycle_on_complete_graph(self):
        g = nx.complete_graph(4)
        assert is_hamiltonian_cycle(g, [0, 1, 2, 3]) is True

    def test_cycle_missing_edge(self):
        g = nx.cycle_graph(4)          # edges: 0-1, 1-2, 2-3, 3-0
        # skipping vertex 3 so the closing edge 2->0 exists but 1->3 does not
        assert is_hamiltonian_cycle(g, [0, 1, 3, 2]) is False

    def test_cycle_wrong_number_of_vertices(self):
        g = nx.complete_graph(4)
        # only 3 distinct vertices in a 4-vertex graph
        assert is_hamiltonian_cycle(g, [0, 1, 2]) is False

    def test_cycle_on_triangle(self):
        g = nx.cycle_graph(3)
        assert is_hamiltonian_cycle(g, [0, 1, 2]) is True


# ---------------------------------------------------------------------------
# is_hamiltonian
# ---------------------------------------------------------------------------

class TestIsHamiltonian:
    def test_complete_graph_k4(self):
        g = nx.complete_graph(4)
        result = is_hamiltonian(g)
        assert result is not False
        assert is_hamiltonian_cycle(g, result) is True

    def test_cycle_graph(self):
        g = nx.cycle_graph(5)
        result = is_hamiltonian(g)
        assert result is not False
        assert is_hamiltonian_cycle(g, result) is True

    def test_disconnected_graph(self):
        g = nx.Graph()
        g.add_nodes_from([0, 1, 2, 3])
        g.add_edges_from([(0, 1), (2, 3)])   # two separate edges – disconnected
        assert is_hamiltonian(g) is False

    def test_too_few_vertices(self):
        g = nx.complete_graph(2)
        assert is_hamiltonian(g) is False

    def test_path_graph_not_hamiltonian(self):
        # A path P4 visits all vertices but cannot close the cycle
        g = nx.path_graph(4)
        assert is_hamiltonian(g) is False


# ---------------------------------------------------------------------------
# is_proper_coloring
# ---------------------------------------------------------------------------

class TestIsProperColoring:
    def test_valid_2_coloring_of_bipartite(self):
        g = nx.complete_bipartite_graph(2, 2)
        # nodes: 0,1 on one side, 2,3 on the other
        coloring = {0: 0, 1: 0, 2: 1, 3: 1}
        assert is_proper_coloring(g, coloring) is True

    def test_invalid_coloring(self):
        g = nx.complete_graph(3)
        # All three nodes have the same colour – every edge is monochromatic
        coloring = {0: 0, 1: 0, 2: 0}
        assert is_proper_coloring(g, coloring) is False

    def test_valid_coloring_triangle(self):
        g = nx.cycle_graph(3)
        coloring = {0: 0, 1: 1, 2: 2}
        assert is_proper_coloring(g, coloring) is True


# ---------------------------------------------------------------------------
# is_3_colorable
# ---------------------------------------------------------------------------

class TestIs3Colorable:
    def test_triangle_is_3_colorable(self):
        g = nx.cycle_graph(3)
        result = is_3_colorable(g)
        assert result is not False

    def test_k4_not_3_colorable(self):
        # K4 requires 4 colours
        g = nx.complete_graph(4)
        assert is_3_colorable(g) is False

    def test_bipartite_graph_is_3_colorable(self):
        g = nx.complete_bipartite_graph(2, 2)
        result = is_3_colorable(g)
        assert result is not False


# ---------------------------------------------------------------------------
# sum_of_values
# ---------------------------------------------------------------------------

class TestSumOfValues:
    def test_all_selected(self):
        assert sum_of_values([3, 5, 7], [1, 1, 1]) == 15

    def test_none_selected(self):
        assert sum_of_values([3, 5, 7], [0, 0, 0]) == 0

    def test_partial_selection(self):
        assert sum_of_values([3, 5, 7], [1, 0, 1]) == 10

    def test_single_element(self):
        assert sum_of_values([42], [1]) == 42

    def test_float_values(self):
        assert sum_of_values([1.5, 2.5], [1, 1]) == pytest.approx(4.0)


# ---------------------------------------------------------------------------
# knapsack_problem
# ---------------------------------------------------------------------------

class TestKnapsackProblem:
    def test_solution_exists(self):
        profits = [3, 5, 7]
        weights = [2, 4, 6]
        result = knapsack_problem(profits, weights, capacity=10, goal=10)
        assert result is not False
        assert sum_of_values(weights, result) <= 10
        assert sum_of_values(profits, result) >= 10

    def test_no_solution_capacity_exceeded(self):
        profits = [3, 5, 7]
        weights = [5, 5, 5]
        # Every item is too heavy to fit two in the bag to reach goal=8
        result = knapsack_problem(profits, weights, capacity=4, goal=8)
        assert result is False

    def test_no_solution_goal_unreachable(self):
        profits = [1, 1, 1]
        weights = [1, 1, 1]
        result = knapsack_problem(profits, weights, capacity=10, goal=100)
        assert result is False

    def test_single_item_solution(self):
        result = knapsack_problem([10], [1], capacity=5, goal=10)
        assert result is not False
        assert result == (1,)

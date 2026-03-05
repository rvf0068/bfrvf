# bfrvf

A small Python library with brute-force implementations of several classical
combinatorial problems.

## Functions

| Function | Description |
|---|---|
| `is_hamiltonian_cycle(graph, cycle)` | Returns `True` if `cycle` is a Hamiltonian cycle in `graph`. |
| `is_hamiltonian(graph)` | Returns a Hamiltonian cycle (tuple of vertices) if one exists, otherwise `False`. |
| `is_proper_coloring(graph, coloring)` | Returns `True` if `coloring` is a proper vertex coloring of `graph`. |
| `is_3_colorable(graph)` | Returns a proper 3-coloring (tuple) if one exists, otherwise `False`. |
| `sum_of_values(values, keys)` | Returns the dot product of `values` and `keys` (a list of 0s and 1s). |
| `knapsack_problem(profits, weights, capacity, goal)` | Returns a 0/1 selection tuple if it meets `goal` profit within `capacity` weight, otherwise `False`. |

All graph arguments are [NetworkX](https://networkx.org/) graph objects.

## Installation

```bash
pip install .
```

## Running the tests

Install the package together with its test dependencies and then run
[pytest](https://docs.pytest.org/):

```bash
pip install ".[test]"
pytest
```

To run a specific test file or test class:

```bash
pytest tests/test_bfrvf.py
pytest tests/test_bfrvf.py::TestIsHamiltonian
```

To run with verbose output:

```bash
pytest -v
```

import itertools

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
import numpy as np
from ks_utils import *


def solve_memoization(items, capacity):
    n = len(items)
    m = np.full((n, capacity + 1), -1)
    # m = [[-1] * (capacity + 1) for _ in range(n + 1)]
    return knapsack_helper(items, m, n, capacity), encuentra(m, items)


def knapsack_helper(items, m, n, capacity):
    if m[n-1, capacity] >= 0:
        return m[n-1, capacity]

    if n == 0:
        q = 0
    elif items[n-1].weight <= capacity:
        q = max(knapsack_helper(items, m, n - 1, capacity - items[n-1].weight) + items[n-1].value,
                knapsack_helper(items, m, n - 1, capacity))
    else:
        q = knapsack_helper(items, m, n - 1, capacity)
    m[n-1, capacity] = q
    return q


def encuentra(matrix, items):
    result = [0]*len(items)
    i, j = len(matrix) - 1, len(matrix[0]) - 1
    while i > 0:
        if matrix[i][j] != matrix[i-1][j]:
            result[i] = 1
            j -= items[i].weight
        i -= 1
    return result
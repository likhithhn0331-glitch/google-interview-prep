def two_sum_bf(array, target):
    """
    Brute force solution to the two sum problem.

    :param array: List of integers
    :param target: Integer target sum
    :return: List containing the indices of the two numbers that add up to the target, or None if no solution exists
    """
    n = len(array)
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] + array[j] == target:
                return [i, j]
    return None
def two_sum_hashmap(array, target):
    """
    Hashmap solution to the two sum problem.

    :param array: List of integers
    :param target: Integer target sum
    :return: List containing the indices of the two numbers that add up to the target, or None if no solution exists
    """
    num_to_index = {}

    for i, num in enumerate(array):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

    return None

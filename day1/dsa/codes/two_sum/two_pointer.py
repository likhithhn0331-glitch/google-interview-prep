def two_sum_two_pointer(array, target):
    """
    Two pointer solution to the two sum problem.

    :param array: List of integers
    :param target: Integer target sum
    :return: List containing the indices of the two numbers that add up to the target, or None if no solution exists
    """
    # Create a list of tuples (value, original_index)
    indexed_array = [(array[i], i) for i in range(len(array))]
    # Sort the list by value
    indexed_array.sort()

    left = 0
    right = len(indexed_array) - 1

    while left < right:
        current_sum = indexed_array[left][0] + indexed_array[right][0]
        if current_sum == target:
            # Return the original indices
            return [indexed_array[left][1], indexed_array[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None

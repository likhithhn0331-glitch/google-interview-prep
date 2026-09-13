def min_sub_array_sum_brute_force(array, target):
    n = len(array)
    min_length = float('inf')

    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += array[end]
            if current_sum >= target:
                min_length = min(min_length, end - start + 1)
                break  # No need to continue this inner loop since we found a valid subarray

    return min_length if min_length != float('inf') else 0

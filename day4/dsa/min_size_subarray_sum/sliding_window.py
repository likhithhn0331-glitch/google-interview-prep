def min_sub_array_sum_sliding_window(array, target):
    n = len(array)
    min_length = float('inf')
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += array[end]

        while current_sum >= target:
            min_length = min(min_length, end - start + 1)
            current_sum -= array[start]
            start += 1

    return min_length if min_length != float('inf') else 0

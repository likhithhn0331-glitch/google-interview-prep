def sub_array_sum_sliding_window(array, k):
    n = len(array)
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += array[end]

        while current_sum > k and start <= end:
            current_sum -= array[start]
            start += 1

        if current_sum == k:
            return True

    return False

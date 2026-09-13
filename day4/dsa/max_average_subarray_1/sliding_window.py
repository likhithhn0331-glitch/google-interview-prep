def max_average_sliding_window(array, k):
    n = len(array)
    if k <= 0 or k > n:
        return None  # Not enough elements for the window size

    # Calculate the sum of the first window
    current_sum = sum(array[:k])
    max_avg = current_sum / k

    # Slide the window across the array
    for i in range(k, n):
        current_sum += array[i] - array[i - k]  # Update the sum for the new window
        current_avg = current_sum / k
        if current_avg > max_avg:
            max_avg = current_avg

    return max_avg

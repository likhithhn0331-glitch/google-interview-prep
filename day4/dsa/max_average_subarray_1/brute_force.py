def max_average_brute_force(array, k):
    n = len(array)
    if k <= 0 or k > n:
        return None

    max_avg = float('-inf')
    for i in range(n - k + 1):
        current_sum = sum(array[i:i + k])
        current_avg = current_sum / k
        if current_avg > max_avg:
            max_avg = current_avg
    return max_avg

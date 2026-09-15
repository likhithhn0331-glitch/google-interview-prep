def sub_array_sum_brute_force(array, k):
    n = len(array)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += array[j]
            if current_sum == k:
                return True
    return False

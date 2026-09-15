def contiguous_array_brute_force(arr):
    n = len(arr)
    max_length = 0
    for i in range(n):
        seen = set()
        current_length = 0
        for j in range(i, n):
            if arr[j] in seen:
                break
            seen.add(arr[j])
            current_length += 1
        max_length = max(max_length, current_length)
    return max_length

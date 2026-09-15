def contiguous_array_prefix_sum(arr):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    max_length = 0
    seen = {}
    for i in range(n + 1):
        if prefix_sum[i] in seen:
            max_length = max(max_length, i - seen[prefix_sum[i]])
        else:
            seen[prefix_sum[i]] = i

    return max_length

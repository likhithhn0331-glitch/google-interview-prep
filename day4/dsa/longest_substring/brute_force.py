def longest_substring_brute_force(s):
    n = len(s)
    max_length = 0
    for i in range(n):
        seen = set()
        current_length = 0
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            current_length += 1
        max_length = max(max_length, current_length)
    return max_length

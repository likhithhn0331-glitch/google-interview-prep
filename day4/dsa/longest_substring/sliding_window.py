def longest_substring_sliding_window(s):
    n = len(s)
    char_index_map = {}
    max_length = 0
    left = 0

    for right in range(n):
        if s[right] in char_index_map and char_index_map[s[right]] >= left:
            left = char_index_map[s[right]] + 1
        char_index_map[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

# DSA - Longest substring without repeating characters

from brute_force import longest_substring_brute_force
from sliding_window import longest_substring_sliding_window

# Test cases for validation
strings = [
    "",
    "a",
    "aa",
    "ab",
    "abcabcbb",
    "bbbbb",
    "pwwkew",
    "dvdf",
    "tmmzuxt",
    "abcdefghijklmnopqrstuvwxyz",
    "abba",
    "abcdefg",
    "au",
    "aab",
    "abca",
    "qrsvbspk",
]

for string in strings:
    print(f"Input string: {string!r}")

    brute_force_result = longest_substring_brute_force(string)
    sliding_window_result = longest_substring_sliding_window(string)

    print("Brute Force Result:", brute_force_result)
    print("Sliding Window Result:", sliding_window_result)
    print("-" * 30)

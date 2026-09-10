# Valid anagram DSA problem
from brute_force import valid_anagram_brute_force
from frequency_counting import valid_anagrams_frequency_counting


def run_test_cases():
    test_cases = [
        ("listen", "silent", True),
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "a", True),
        ("", "", True),
        ("ab", "a", False),
        ("aacc", "ccaa", True),
        ("abca", "abdc", False),
        ("leetcode", "codeleet", True),
    ]

    for str_1, str_2, expected in test_cases:
        brute_force_result = valid_anagram_brute_force(str_1, str_2)
        frequency_result = valid_anagrams_frequency_counting(str_1, str_2)

        assert brute_force_result == expected, (
            f"Brute force failed for '{str_1}' and '{str_2}': "
            f"expected {expected}, got {brute_force_result}"
        )
        assert frequency_result == expected, (
            f"Frequency counting failed for '{str_1}' and '{str_2}': "
            f"expected {expected}, got {frequency_result}"
        )

        print(f"'{str_1}' and '{str_2}' -> {expected}")

    print("\nAll valid anagram test cases passed.")


if __name__ == "__main__":
    str_1 = "listen"
    str_2 = "silent"

    print("Using Frequency Counting Method:")
    if valid_anagrams_frequency_counting(str_1, str_2):
        print(f'"{str_1}" and "{str_2}" are valid anagrams.')
    else:
        print(f'"{str_1}" and "{str_2}" are not valid anagrams.')

    print("\nUsing Brute Force Method:")
    if valid_anagram_brute_force(str_1, str_2):
        print(f'"{str_1}" and "{str_2}" are valid anagrams.')
    else:
        print(f'"{str_1}" and "{str_2}" are not valid anagrams.')

    run_test_cases()
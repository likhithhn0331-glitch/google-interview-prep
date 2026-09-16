from brute_force import group_anagrams_brute_force
from hashing_interval import group_anagrams_hashing_interval


TEST_CASES = [
    {
        "name": "Example 1",
        "input": ["eat", "tea", "tan", "ate", "nat", "bat"],
        "expected": [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
    },
    {
        "name": "Example 2",
        "input": [""],
        "expected": [[""]],
    },
    {
        "name": "Example 3",
        "input": ["a"],
        "expected": [["a"]],
    },
    {
        "name": "Example 4",
        "input": ["abc", "bca", "cab", "xyz"],
        "expected": [["abc", "bca", "cab"], ["xyz"]],
    },
    {
        "name": "Example 5",
        "input": ["a", "a", "a"],
        "expected": [["a", "a", "a"]],
    },
    {
        "name": "Example 6",
        "input": ["listen", "silent", "enlist", "google"],
        "expected": [["listen", "silent", "enlist"], ["google"]],
    },
]


def normalize_groups(groups):
    """Ignore group order while preserving duplicates within each group."""
    normalized = []
    for group in groups:
        normalized.append(tuple(sorted(group)))
    return sorted(normalized)


def compare_solutions():
    print("Running group-anagram test cases...\n")

    all_passed = True
    for case in TEST_CASES:
        brute_result = group_anagrams_brute_force(case["input"])
        hashing_result = group_anagrams_hashing_interval(case["input"])
        expected = case["expected"]

        brute_ok = normalize_groups(brute_result) == normalize_groups(expected)
        hashing_ok = normalize_groups(hashing_result) == normalize_groups(expected)
        both_match = normalize_groups(brute_result) == normalize_groups(hashing_result)

        status = "PASS" if brute_ok and hashing_ok and both_match else "FAIL"
        if status == "FAIL":
            all_passed = False

        print(f"{case['name']}: {status}")
        print(f"  Input: {case['input']}")
        print(f"  Expected: {expected}")
        print(f"  Brute Force: {brute_result}")
        print(f"  Hashing: {hashing_result}")
        print()

        if not (brute_ok and hashing_ok and both_match):
            if not brute_ok:
                print("  Brute force output does not match expected.")
            if not hashing_ok:
                print("  Hashing output does not match expected.")
            if not both_match:
                print("  Solutions produce different groupings.")
            print()

    print("Summary:")
    if all_passed:
        print("All group-anagram test cases passed for both solutions.")
    else:
        print("One or more test cases failed.")

    print("\nComplexity comparison:")
    print("- Brute force: O(n^2 * k log k) due to repeated sorting comparisons.")
    print("- Hashing interval: O(L) to build frequency signatures, then O(n) to group by key.")
    print("  (Where n = number of strings and L = total number of characters across all strings.)")


if __name__ == "__main__":
    compare_solutions()

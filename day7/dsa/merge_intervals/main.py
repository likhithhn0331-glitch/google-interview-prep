from brute_force import merge_intervals_brute_force
from hashing_interval import merge_intervals_hashing_interval


TEST_CASES = [
    {
        "name": "Example 1",
        "input": [[1, 3], [2, 6], [8, 10], [9, 12]],
        "expected": [[1, 6], [8, 12]],
    },
    {
        "name": "Example 2 - Unsorted",
        "input": [[8, 10], [1, 3], [2, 6], [9, 12]],
        "expected": [[1, 6], [8, 12]],
    },
    {
        "name": "Example 3 - Separate",
        "input": [[1, 2], [4, 5], [7, 9]],
        "expected": [[1, 2], [4, 5], [7, 9]],
    },
    {
        "name": "Example 4 - Nested",
        "input": [[1, 10], [2, 5], [3, 7], [4, 9]],
        "expected": [[1, 10]],
    },
    {
        "name": "Example 5 - Boundary touching",
        "input": [[1, 3], [3, 5]],
        "expected": [[1, 5]],
    },
    {
        "name": "Example 6 - Single interval",
        "input": [[1, 5]],
        "expected": [[1, 5]],
    },
    {
        "name": "Example 7 - Empty input",
        "input": [],
        "expected": [],
    },
    {
        "name": "Example 8 - Reversed bounds",
        "input": [[9, 4], [2, 8], [6, 1]],
        "expected": [[1, 9]],
    },
]


def normalize_intervals(intervals):
    """Sort intervals and normalize them for reliable comparison."""
    if not intervals:
        return []
    return sorted(tuple(interval) for interval in intervals)


def compare_solutions():
    print("Running merge-interval test cases...\n")
    all_passed = True

    for case in TEST_CASES:
        brute_result = merge_intervals_brute_force(case["input"])
        hashing_result = merge_intervals_hashing_interval(case["input"])
        expected = case["expected"]

        brute_ok = normalize_intervals(brute_result) == normalize_intervals(expected)
        hashing_ok = normalize_intervals(hashing_result) == normalize_intervals(expected)
        both_match = normalize_intervals(brute_result) == normalize_intervals(hashing_result)

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
                print("  Solutions produce different merged intervals.")
            print()

    print("Summary:")
    if all_passed:
        print("All merge-interval test cases passed for both solutions.")
    else:
        print("One or more test cases failed.")

    print("\nComplexity comparison:")
    print("- Brute force: O(n^2) pairwise overlap checks.")
    print("- Hashing-based interval coverage: O(total covered integer range) with set membership.")
    print("  This is easy to reason about but can be more expensive when intervals span large ranges.")


if __name__ == "__main__":
    compare_solutions()

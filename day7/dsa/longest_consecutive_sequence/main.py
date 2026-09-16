from brute_force import longest_consecutive_sequence_brute_force
from hashing_interval import longest_consecutive_sequence_hashing_interval


TEST_CASES = [
    {
        "name": "Example 1",
        "input": [100, 4, 200, 1, 3, 2],
        "expected": 4,
    },
    {
        "name": "Example 2",
        "input": [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
        "expected": 9,
    },
    {
        "name": "Example 3",
        "input": [],
        "expected": 0,
    },
    {
        "name": "Example 4",
        "input": [1],
        "expected": 1,
    },
    {
        "name": "Example 5",
        "input": [9, 1, 4, 7, 3, -1, 0, 5, 8, -2, 6, 0, 2],
        "expected": 12,
    },
    {
        "name": "Edge case: duplicates",
        "input": [1, 1, 2, 2, 3, 3],
        "expected": 3,
    },
    {
        "name": "Edge case: negatives",
        "input": [-1, 0, 1, 2, 4, 5, 7, 8, 9],
        "expected": 4,
    },
    {
        "name": "Edge case: all same",
        "input": [5, 5, 5],
        "expected": 1,
    },
]


def compare_solutions():
    print("Running longest-consecutive-sequence test cases...\n")

    all_passed = True
    for case in TEST_CASES:
        brute_result = longest_consecutive_sequence_brute_force(case["input"])
        hashing_result = longest_consecutive_sequence_hashing_interval(case["input"])
        expected = case["expected"]

        brute_ok = brute_result == expected
        hashing_ok = hashing_result == expected
        both_match = brute_result == hashing_result

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
                print("  Solutions produce different results.")
            print()

    print("Summary:")
    if all_passed:
        print("All longest-consecutive-sequence test cases passed for both solutions.")
    else:
        print("One or more test cases failed.")

    print("\nComplexity comparison:")
    print("- Brute force: O(n^2) time because each unique value may scan upward.")
    print("- Hashing interval: O(n) time using a set for constant-time checks.")


if __name__ == "__main__":
    compare_solutions()

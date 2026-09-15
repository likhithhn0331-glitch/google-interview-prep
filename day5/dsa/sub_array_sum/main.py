from brute_force import sub_array_sum_brute_force
from sliding_window import sub_array_sum_sliding_window


# Test cases valid for both approaches:
# the sliding window solution only works for non-negative numbers.
test_cases = [
    ([1, 2, 3, 4, 5], 9, True),
    ([1, 1, 1], 2, True),
    ([1, 2, 3], 7, False),
    ([1, 2, 3], 10, False),
    ([2, 2, 2], 4, True),
    ([0, 0, 0, 0], 0, True),
    ([1, 2, 3, 4, 5], 15, True),
    ([2, 2, 2], 5, False),
]


def compare_solutions():
    for index, (nums, k, expected) in enumerate(test_cases, start=1):
        brute_result = sub_array_sum_brute_force(nums, k)
        window_result = sub_array_sum_sliding_window(nums, k)

        print(f"Test case {index}: nums={nums}, k={k}")
        print(f"  brute force: {brute_result}")
        print(f"  sliding window: {window_result}")

        if brute_result != expected or window_result != expected:
            print(f"  FAILED: expected {expected}")
            raise AssertionError(f"Mismatch in test case {index}")

        if brute_result != window_result:
            print(f"  FAILED: solutions disagree")
            raise AssertionError(f"Solutions disagree in test case {index}")

        print("  PASS")

    print("\nAll test cases passed for both solutions.")


if __name__ == "__main__":
    compare_solutions()

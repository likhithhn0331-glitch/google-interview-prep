from brute_force import continuous_subarray_brute_force
from prefix_sum import continuous_subarray_prefix_sum


def compare_solutions(test_cases):
    """Run both algorithms on the same inputs and verify they match."""
    for index, (nums, k, expected) in enumerate(test_cases, start=1):
        brute_result = continuous_subarray_brute_force(nums, k)
        optimized_result = continuous_subarray_prefix_sum(nums, k)

        print(f"Test {index}: nums={nums}, k={k}")
        print(f"  brute_force: {brute_result}")
        print(f"  optimized:   {optimized_result}")

        if brute_result != optimized_result:
            raise AssertionError(
                f"Mismatch on test {index}: brute={brute_result}, optimized={optimized_result}"
            )

        if expected is not None and brute_result != expected:
            raise AssertionError(
                f"Expected {expected} but got {brute_result} on test {index}"
            )

        print("  status: PASS")

    print("\nAll test cases passed for both solutions.")


if __name__ == "__main__":
    test_cases = [
        ([23, 2, 4, 6, 7], 6, True),
        ([23, 2, 6, 4, 7], 6, True),
        ([1, 2, 3], 5, True),
        ([1, 1, 1], 2, True),
        ([1, 2, 3], 1, True),
        ([-1, -1], 2, True),
        ([0, 0], 0, True),
        ([1, 0, 1], 2, True),
        ([1, 2, 1], 2, True),
        ([1, 3, 5], 3, True),
        ([2, 2], 2, True),
        ([1, 1], 0, False),
    ]

    compare_solutions(test_cases)

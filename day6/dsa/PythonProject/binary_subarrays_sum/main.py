from collections import defaultdict


def brute_force_count(nums, goal):
    """Count subarrays whose sum equals goal by checking every subarray."""
    count = 0
    n = len(nums)
    for left in range(n):
        current_sum = 0
        for right in range(left, n):
            current_sum += nums[right]
            if current_sum == goal:
                count += 1
    return count


def prefix_sum_count(nums, goal):
    """Optimized O(n) solution using prefix sums and a frequency map."""
    prefix_sum = 0
    count = 0
    freq = defaultdict(int)
    freq[0] = 1

    for num in nums:
        prefix_sum += num
        count += freq.get(prefix_sum - goal, 0)
        freq[prefix_sum] += 1

    return count


def compare_solutions(test_cases):
    """Run both algorithms on the same inputs and verify they match."""
    for index, (nums, goal, expected) in enumerate(test_cases, start=1):
        brute_result = brute_force_count(nums, goal)
        optimized_result = prefix_sum_count(nums, goal)

        print(f"Test {index}: nums={nums}, goal={goal}")
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
        ([1, 0, 1, 0, 1], 2, 4),
        ([0, 0, 0, 0, 0], 0, 15),
        ([1, 1, 1], 2, 2),
        ([0, 1, 0, 1], 1, 6),
        ([1, 0, 0, 1], 1, 6),
        ([1], 0, 0),
        ([0], 0, 1),
        ([1, 0, 1], 1, 4),
    ]

    compare_solutions(test_cases)

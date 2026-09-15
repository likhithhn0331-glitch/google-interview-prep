# DSA PROBLEM — Product of Array Except Self

from time import perf_counter


def product_except_self_bruteforce(nums):
    """O(n^2) brute-force approach."""
    n = len(nums)
    result = [0] * n

    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result[i] = product

    return result


def product_except_self_prefix_suffix(nums):
    """O(n) optimized approach using prefix and suffix products."""
    n = len(nums)
    if n == 0:
        return []

    result = [1] * n

    # product of elements to the left of each index
    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


def run_test_cases():
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([5], [1]),
        ([1, 0, 3, 4], [0, 12, 0, 0]),
        ([0, 0, 5], [0, 0, 0]),
        ([-1, 2, -3, 4], [-24, 12, -8, 6]),
        ([2, 2, 2, 2], [8, 8, 8, 8]),
        ([3, -1, 2, 4], [-8, 24, -12, -6]),
        ([], []),
    ]

    for idx, (nums, expected) in enumerate(test_cases, start=1):
        brute = product_except_self_bruteforce(nums)
        optimized = product_except_self_prefix_suffix(nums)

        assert brute == expected, f"Bruteforce failed for case {idx}: {nums} -> {brute} != {expected}"
        assert optimized == expected, f"Optimized failed for case {idx}: {nums} -> {optimized} != {expected}"

    print("All test cases passed.")


def compare_algorithms():
    sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    start = perf_counter()
    brute = product_except_self_bruteforce(sample)
    brute_time = perf_counter() - start

    start = perf_counter()
    optimized = product_except_self_prefix_suffix(sample)
    optimized_time = perf_counter() - start

    print(f"Sample input: {sample}")
    print(f"Brute force result: {brute}")
    print(f"Optimized result:   {optimized}")
    print(f"Brute force time: {brute_time:.8f}s")
    print(f"Optimized time:   {optimized_time:.8f}s")
    print("\nComplexity comparison:")
    print("- Brute force: O(n^2) time, O(1) extra space")
    print("- Prefix + suffix: O(n) time, O(1) extra space (excluding output array)")


if __name__ == "__main__":
    run_test_cases()
    print()
    compare_algorithms()

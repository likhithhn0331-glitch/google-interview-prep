"""
DSA problem: Minimum size subarray sum

This file contains two solution variants and a set of test cases that run both
implementations and print their outputs for comparison.
"""

from typing import List


def min_subarray_len_sliding(target: int, nums: List[int]) -> int:
    """Sliding window O(n) solution."""
    n = len(nums)
    left = 0
    curr = 0
    res = float('inf')
    for right in range(n):
        curr += nums[right]
        while curr >= target:
            res = min(res, right - left + 1)
            curr -= nums[left]
            left += 1
    return 0 if res == float('inf') else res


def min_subarray_len_prefix_binary(target: int, nums: List[int]) -> int:
    """Prefix sums + binary search O(n log n) solution."""
    import bisect

    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    res = float('inf')
    for i in range(n):
        need = target + prefix[i]
        j = bisect.bisect_left(prefix, need)
        if j <= n:
            res = min(res, j - i)
    return 0 if res == float('inf') else res


# Test cases: (target, nums, name)
tests = [
    (7, [2, 3, 1, 2, 4, 3], "example1"),
    (4, [1, 4, 4], "example2"),
    (11, [1, 1, 1, 1, 1, 1, 1, 1], "example3"),
    (3, [1, 2], "small"),
    (5, [5], "single_exact"),
    (6, [7], "single_gt"),
    (15, [1, 2, 3, 4, 5], "sum_all"),
    (100, [10] * 9, "no_solution"),
]


if __name__ == "__main__":
    for target, nums, name in tests:
        a = min_subarray_len_sliding(target, nums)
        b = min_subarray_len_prefix_binary(target, nums)
        print(f"Test {name}: target={target}, nums={nums}")
        print(f"  sliding -> {a}")
        print(f"  prefix+bin -> {b}\n")

"""
Given an integer array nums and an integer k, return true if there is a contiguous subarray
of length at least 2 whose sum is a multiple of k.
"""


def continuous_subarray_brute_force(nums, k):
    """Check if there is a contiguous subarray of length at least 2 whose sum is a multiple of k."""
    n = len(nums)
    for left in range(n):
        current_sum = 0
        for right in range(left, n):
            current_sum += nums[right]
            subarray_length = right - left + 1
            if subarray_length >= 2:
                if k == 0:
                    if current_sum == 0:
                        return True
                elif current_sum % k == 0:
                    return True
    return False

"""
Given an integer array nums and an integer k, return true if there is a contiguous subarray
of length at least 2 whose sum is a multiple of k.
"""


def continuous_subarray_prefix_sum(nums, k):
    """Check if there is a contiguous subarray of length at least 2 whose sum is a multiple of k."""
    prefix_sum = 0
    seen = {0: -1}

    for i, num in enumerate(nums):
        prefix_sum += num

        if k == 0:
            if prefix_sum in seen:
                if i - seen[prefix_sum] >= 2:
                    return True
            else:
                seen[prefix_sum] = i
            continue

        remainder = prefix_sum % k
        if remainder in seen:
            if i - seen[remainder] >= 2:
                return True
        else:
            seen[remainder] = i

    return False

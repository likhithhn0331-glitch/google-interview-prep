# Given an unsorted array of integers nums, find the length of the longest
# consecutive sequence.

def longest_consecutive_sequence_brute_force(nums):
    """
    Brute-force solution.

    For each number, check if it starts a sequence by walking upward until the
    next value is not present. Track the maximum length found.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    if not nums:
        return 0

    longest = 1
    unique_nums = set(nums)

    for num in unique_nums:
        if num - 1 not in unique_nums:
            current_length = 1
            while num + current_length in unique_nums:
                current_length += 1
            longest = max(longest, current_length)

    return longest

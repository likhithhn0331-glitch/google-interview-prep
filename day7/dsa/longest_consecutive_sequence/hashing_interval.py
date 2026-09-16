# Given an unsorted array of integers nums, find the length of the longest
# consecutive sequence.

def longest_consecutive_sequence_hashing_interval(nums):
    """
    Hashing-based interval solution.

    Use a set for O(1) lookups. Only expand from the beginning of each sequence,
    which avoids redundant work for numbers that are not sequence starts.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    if not nums:
        return 0

    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            current = num
            streak = 1
            while current + 1 in num_set:
                current += 1
                streak += 1
            longest = max(longest, streak)

    return longest

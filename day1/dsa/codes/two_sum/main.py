# Two sum DSA problem
from brute_force import two_sum_bf
from two_pointer import two_sum_two_pointer
from hashmap import two_sum_hashmap
import time

# Common LeetCode-style test cases for Two Sum
# Format: (nums, target, expected_indices)
leetcode_test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([1, 3, 4, 5], 8, [1, 3]),
    ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ([10, 20, 30, 40], 50, [0, 3]),
]

for index, (nums, target, expected) in enumerate(leetcode_test_cases, start=1):
    print(f"\nTest case {index}: nums={nums}, target={target}")

    start = time.time()
    brute_result = two_sum_bf(nums, target)
    brute_time = time.time() - start
    print(f"Brute force: {brute_result} | Time: {brute_time:.8f}s")

    start = time.time()
    hashmap_result = two_sum_hashmap(nums, target)
    hashmap_time = time.time() - start
    print(f"Hashmap: {hashmap_result} | Time: {hashmap_time:.8f}s")

    start = time.time()
    two_pointer_result = two_sum_two_pointer(nums, target)
    two_pointer_time = time.time() - start
    print(f"Two pointer: {two_pointer_result} | Time: {two_pointer_time:.8f}s")

    print(f"Expected: {expected}")

# Continuous Subarray

Problem
-------
Given an integer array `nums` and an integer `k`, return `true` if there is a contiguous subarray of length at least `2` whose sum is a multiple of `k`.

A subarray sum is a multiple of `k` if:
- `sum % k == 0` when `k != 0`, or
- the subarray sum is exactly `0` when `k == 0`.

Examples
--------
Example 1:
Input: nums = [23, 2, 4, 6, 7], k = 6
Output: true
Explanation: The subarray [2, 4] has sum 6, which is divisible by 6.

Example 2:
Input: nums = [23, 2, 6, 4, 7], k = 6
Output: true
Explanation: The subarray [23, 2, 6, 4, 7] has sum 42, which is divisible by 6.

Example 3:
Input: nums = [1, 2, 3], k = 5
Output: false
Explanation: No contiguous subarray of length at least 2 has a sum divisible by 5.

Constraints
-----------
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^9

Notes & Hints
-------------
- Use prefix sums to track cumulative totals as you scan the array.
- For a fixed `k`, only the remainder modulo `k` matters.
- If two prefix sums have the same remainder, the difference between them is a multiple of `k`.
- Store the first index where each remainder appears so you can check the subarray length.
- A valid subarray must have length at least 2, so you need to verify the distance between matching prefix sums is at least 2.

Suggested solution outline
-------------------------
1. Initialize `prefix_sum = 0` and a map `first_seen = {0: -1}`.
2. Walk through the array from left to right with index `i`.
3. Update `prefix_sum += nums[i]`.
4. If `k != 0`, compute `remainder = prefix_sum % k`.
5. If `remainder` has already appeared before, check whether `i - first_seen[remainder] >= 2`.
6. If it is, return `true`.
7. Otherwise, store the current index for that remainder if it has not been seen yet.
8. If no valid subarray is found, return `false`.
9. Handle the special case `k == 0` by checking when the running sum becomes zero at two different positions at least 2 apart.

Why this works
--------------
If two prefix sums have the same remainder modulo `k`, their difference is divisible by `k`. That difference corresponds to a contiguous subarray whose total sum is a multiple of `k`.

By storing the earliest index for each remainder, we can detect repeated remainders and confirm the subarray length is at least 2.

Complexity
----------
- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

Optional: include unit tests with edge cases such as:
- all positive numbers
- negative numbers
- repeated values
- single-element arrays
- `k = 1`
- `k = 0`

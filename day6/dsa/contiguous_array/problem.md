# Contiguous Array

Problem
-------
Given a binary array nums (each element is 0 or 1), find the maximum length of a contiguous subarray with an equal number of 0s and 1s.

Return the length of the longest contiguous subarray that contains an equal number of 0 and 1.

Examples
--------
Example 1:
Input: nums = [0,1]
Output: 2
Explanation: The whole array has one 0 and one 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: The longest subarray with equal numbers is [0,1] or [1,0].

Constraints
-----------
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1

Notes & Hints
-------------
- Convert 0 to -1 and then find the longest subarray with sum 0. This transforms the problem into finding the longest contiguous subarray whose prefix sums repeat.
- Use a hashmap (dictionary) to record the first index where each prefix sum occurs. When the same sum reappears, the subarray between the first occurrence+1 and the current index has sum 0.
- Time complexity: O(n). Space complexity: O(n).

Suggested solution outline
--------------------------
1. Initialize a running sum `sum = 0` and a map `firstIndex` that stores `sum -> index`. Put `firstIndex[0] = -1` to handle subarrays starting at index 0.
2. Iterate i from 0 to n-1:
   - If nums[i] == 0, add -1 to `sum`; otherwise add +1.
   - If `sum` is already in `firstIndex`, compute candidate length `i - firstIndex[sum]` and update max length.
   - Otherwise, store `firstIndex[sum] = i`.
3. Return the max length found.

Optional: include unit tests with edge cases such as all 0s, all 1s, alternating patterns, and single-element arrays.

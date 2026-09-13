# Minimum Size Subarray Sum

Problem (LeetCode 209):
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [nums[l], nums[l+1], ..., nums[r]] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Input:
- nums: array of positive integers (length n)
- target: positive integer

Output:
- The minimal length (integer) of a contiguous subarray with sum >= target, or 0 if none exists.

Examples:
1) Input: target = 7, nums = [2,3,1,2,4,3]
   Output: 2
   Explanation: The subarray [4,3] has sum 7 and length 2.

2) Input: target = 4, nums = [1,4,4]
   Output: 1

3) Input: target = 11, nums = [1,1,1,1,1,1,1,1]
   Output: 0

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
- 1 <= target <= 10^9

Expected complexity:
- Optimal: O(n) time and O(1) extra space using sliding window (two pointers).

Hints / Approach:
- Use two pointers (left, right) and a running sum. Expand right until sum >= target, then shrink left to minimize length while maintaining sum >= target. Track the smallest window length found.
- A binary-search on prefix sums can also achieve O(n log n).

Function signatures:
- Python: def min_subarray_len(target: int, nums: List[int]) -> int
- Java: public int minSubArrayLen(int target, int[] nums)
- C++: int minSubArrayLen(int target, vector<int>& nums);

Edge cases:
- Single element equal or greater than target -> return 1
- All elements smaller and total sum < target -> return 0

References: Classic sliding-window problem (LeetCode 209).
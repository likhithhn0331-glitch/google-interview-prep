# Binary Subarrays With Sum

Problem
-------
Given a binary array `nums` (where each element is either `0` or `1`) and an integer `goal`, return the number of non-empty subarrays whose sum is equal to `goal`.

Since all values are `0` or `1`, the sum of a subarray is simply the number of `1`s in that subarray.

Examples
--------
Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The subarrays with sum 2 are:
- [1,0,1]
- [1,0,1]
- [0,1,0,1]
- [1,0,1]

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15
Explanation: Every subarray has sum 0, and there are 15 such non-empty subarrays.

Constraints
-----------
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1
- 0 <= goal <= nums.length

Notes & Hints
-------------
- Use prefix sums. For each index `i`, let `prefix[i]` be the sum of the first `i` elements.
- A subarray from `l` to `r` has sum `goal` exactly when:
  `prefix[r + 1] - prefix[l] = goal`
- This can be rewritten as:
  `prefix[r + 1] = prefix[l] + goal`
- Maintain a frequency map of seen prefix sums while traversing the array.
- For each current prefix sum `prefix_sum`, add the number of previous prefix sums equal to `prefix_sum - goal`.
- This gives a linear-time solution: `O(n)` time and `O(n)` space in the worst case.

Suggested solution outline
-------------------------
1. Initialize `prefix_sum = 0` and a `Counter` (or dictionary) `freq = {0: 1}`.
2. Initialize `answer = 0`.
3. Traverse the array from left to right:
   - Add `nums[i]` to `prefix_sum`.
   - Compute `target = prefix_sum - goal`.
   - Add `freq.get(target, 0)` to `answer`.
   - Increment `freq[prefix_sum]`.
4. Return `answer`.

Why this works
--------------
If a previous prefix sum was `prefix_sum - goal`, then the difference between the current prefix sum and that earlier prefix sum is exactly `goal`.
That difference corresponds to one valid subarray whose sum equals the target value.

Complexity
----------
- Time Complexity: `O(n)`
- Space Complexity: `O(n)`

Optional: include unit tests with edge cases such as:
- all zeros
- all ones
- alternating values
- single-element arrays
- goal = 0

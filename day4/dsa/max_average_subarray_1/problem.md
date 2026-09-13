# Maximum Average Subarray I

## Problem Statement

You are given an integer array `nums` and an integer `k`.

Find the contiguous subarray of length `k` whose average is maximum, and return that maximum average.

A subarray is contiguous, meaning it uses consecutive elements from the array.

For example:

```text
array = [1, 12, -5, -6, 50, 3]
k = 4
```

Possible windows of length 4 are:

1. `[1, 12, -5, -6]` -> average = `(1 + 12 - 5 - 6) / 4 = 0.5`
2. `[12, -5, -6, 50]` -> average = `(12 - 5 - 6 + 50) / 4 = 12.75`
3. `[-5, -6, 50, 3]` -> average = `(-5 - 6 + 50 + 3) / 4 = 10.5`

The maximum average is `12.75`.

---

## Understanding the Problem

We are not asked to return the subarray itself, only the maximum average value.

This is a classic sliding window problem because:

- The window size is fixed (`k`), so every valid subarray has exactly `k` elements.
- As we move from one window to the next, the window overlaps heavily.
- Instead of recomputing the sum from scratch every time, we can update the sum in constant time.

---

## Input/Output Example

### Example 1

```text
Input: nums = [1, 12, -5, -6, 50, 3], k = 4
Output: 12.75
```

### Example 2

```text
Input: nums = [5], k = 1
Output: 5.0
```

### Example 3

```text
Input: nums = [1, 2, 3, 4], k = 2
Output: 3.5
```

Explanation: the best window is `[3, 4]` because its average is `(3 + 4) / 2 = 3.5`.

---

## Constraints

Typical constraints for this problem are:

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

These constraints are large enough that an `O(n * k)` brute force approach will be too slow, so we need an efficient `O(n)` solution.

---

## Brute Force Perspective

The simplest way to think about this problem is to consider every valid subarray of length `k`:

1. Pick every starting index `i` from `0` to `n - k`.
2. Look at the window `nums[i : i + k]`.
3. Compute its sum and divide by `k`.
4. Keep track of the largest average seen so far.

This approach is easy to understand, but it does unnecessary repeated work because windows overlap heavily.

For example, in an array like:

```text
[1, 12, -5, -6, 50, 3]
```

with `k = 4`, the windows are:

- `[1, 12, -5, -6]`
- `[12, -5, -6, 50]`
- `[-5, -6, 50, 3]`

Notice how each window shares most of its elements with the next one. A more efficient method should take advantage of this overlap.

---

## Efficient Observation: Sliding Window

A fixed-size window has a very useful property:

- when the window moves one step to the right,
- only one element leaves the window,
- and one new element enters the window.

So instead of recomputing the full sum of the entire window each time, we can update it in constant time.

If the current window sum is `S`, and the window shifts from:

```text
[a, b, c, d]
to
[b, c, d, e]
```

then the new sum becomes:

```text
new_sum = old_sum - a + e
```

This is the core idea behind the sliding window technique.

---

## Why the Average Depends on the Sum

The problem asks for the maximum average of a window of fixed length `k`.

Since `k` stays constant for all windows, maximizing the average is equivalent to maximizing the sum of the window.

```text
average = sum(window) / k
```

Because `k` is the same denominator for every candidate subarray, we only need to compare window sums.

---

## Step-by-Step Example

Consider:

```text
nums = [1, 12, -5, -6, 50, 3]
k = 4
```

The valid windows are:

1. `[1, 12, -5, -6]`
   - Sum = `1 + 12 - 5 - 6 = 2`
   - Average = `2 / 4 = 0.5`

2. `[12, -5, -6, 50]`
   - Sum = `12 - 5 - 6 + 50 = 51`
   - Average = `51 / 4 = 12.75`

3. `[-5, -6, 50, 3]`
   - Sum = `-5 - 6 + 50 + 3 = 42`
   - Average = `42 / 4 = 10.5`

The maximum average is clearly `12.75`.

This example demonstrates why the window must be moved systematically rather than by checking every possible segment independently.

---

## Core Idea Behind the Solution

The trick is to keep a moving window of exactly `k` elements and maintain its sum while sliding across the array.

At each step:

- add the element entering the window,
- remove the element leaving the window,
- compare the current sum to the best seen so far.

This ensures that every valid window is considered exactly once while preserving efficiency.

---

## Constraints and Why Efficiency Matters

The array size can be large, so a naive approach that recomputes sums for every window may become too slow.

The goal is to avoid repeated work and process the array in a single pass after the initial window is built.

The fixed-size window pattern is the standard way to handle this kind of problem efficiently.

---

## Edge Cases to Consider

- `k == 1`: then the maximum average is simply the maximum element in the array.
- `k == n`: there is only one valid window, the whole array.
- Negative numbers: the window sum can be negative, but the same sliding logic still works.
- Repeated values: multiple windows may tie for the same average.
- Large inputs: the solution must avoid `O(n * k)` behavior.

---

## Interview Focus

This is a classic sliding window problem. When you see a phrase like:

- fixed-length subarray,
- contiguous segment,
- maximum average,
- or overlapping windows,

think about maintaining a running sum and sliding the window instead of recomputing everything.

The key insight is not just the average formula, but the fact that the window changes in a predictable way as it moves.

---

## Summary

The problem is about finding the window of fixed length `k` with the highest average.

The essential idea is:

- keep a window of size `k`,
- maintain its sum efficiently,
- slide it across the array,
- and track the best average.

This reduces unnecessary work and makes the problem efficient for large inputs.

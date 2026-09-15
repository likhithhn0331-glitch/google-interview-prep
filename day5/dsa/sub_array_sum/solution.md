# Solution Guide: Subarray Sum Equals K

## Problem Recap

We are given an array and a target value `k`. The goal is to determine whether a contiguous subarray sums to `k`.

For the current codebase, the two main approaches are:

1. Brute force enumeration
2. Sliding window technique

The prefix-sum + hash map approach is the more general interview-friendly solution for counting subarrays whose sum is exactly `k`, especially when the array may contain negative numbers.

---

## Solution 1: Brute Force

### Idea

Try every possible starting index and expand the end index until the subarray sum is computed.

If the running sum equals `k`, return `True`.

### Python Implementation

```python
def sub_array_sum_brute_force(array, k):
    n = len(array)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += array[j]
            if current_sum == k:
                return True
    return False
```

### Why it works

The outer loop fixes the left boundary `i`, and the inner loop checks every contiguous subarray beginning at `i`.

Every subarray is examined exactly once, so if any subarray sums to `k`, the function will find it.

### Complexity

- Time complexity: `O(n^2)`
  - There are `n` possible starting points and up to `n` possible ending points for each.
- Space complexity: `O(1)`
  - We only use a few variables like `current_sum` and loop indices.

### When to use it

- Small arrays
- For understanding the problem conceptually
- As a baseline before optimizing

### Limitation

This approach is too slow for large inputs because it checks all possible subarrays.

---

## Solution 2: Sliding Window

### Idea

Use two pointers: `start` and `end`.

- Expand the window by adding `array[end]`
- If the sum becomes greater than `k`, shrink the window from the left by subtracting `array[start]`
- Once the window sum equals `k`, return `True`

This works efficiently when all numbers are non-negative.

### Python Implementation

```python
def sub_array_sum_sliding_window(array, k):
    n = len(array)
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += array[end]

        while current_sum > k and start <= end:
            current_sum -= array[start]
            start += 1

        if current_sum == k:
            return True

    return False
```

### Why it works

The sliding window maintains a contiguous segment whose sum is tracked incrementally.

- When the sum grows beyond `k`, we move the left pointer forward to reduce the sum.
- If the sum equals `k`, we found a valid subarray.
- Because the window only moves forward, each element is processed a constant number of times.

### Complexity

- Time complexity: `O(n)`
  - Each pointer moves at most `n` times.
- Space complexity: `O(1)`
  - We only keep a few variables.

### Important note

The sliding window method is valid only when all numbers are non-negative.

If the array contains negative numbers, the sum can increase or decrease unexpectedly, and shrinking the window from the left is not always correct.

Example of when it fails:

```python
array = [3, -2, 1]
k = 1
```

The best window may require a different structure than simple left shrinking.

---

## Prefix Sum + Hash Map: The Interview-Optimal Solution

Although the repo currently uses brute force and sliding window, the most important interview pattern for this problem is:

```text
prefix[j] - prefix[i] = k
```

This means:

- `prefix[j]` is the sum up to index `j`
- `prefix[i]` is the sum up to index `i`
- if their difference equals `k`, then the subarray in between sums to `k`

### Core Insight

If the current prefix sum is `S`, then we need a previous prefix sum of `S - k`.

So while iterating:

- keep the current prefix sum
- check how many times `current_prefix_sum - k` has appeared before
- add that count to the answer

### Why this is important

This works for arrays with negative numbers and allows us to count all valid subarrays, not just check existence.

### Time and space

- Time complexity: `O(n)`
- Space complexity: `O(n)`

---

## Comparing Both Solutions

### Brute force

Pros:

- Simple and easy to understand
- Great for proving the concept
- Good as a baseline

Cons:

- Very slow for large data
- `O(n^2)` time is not interview-friendly for large inputs

### Sliding window

Pros:

- Fast: `O(n)`
- Constant extra space
- Best when the array is non-negative

Cons:

- Fails for negative numbers
- Only works for sum conditions tied to a monotonic moving window

### Best general solution

For the problem statement "subarray sum equals k" in interviews, the prefix sum + hash map is usually the best answer because it:

- handles negatives
- counts all valid subarrays
- runs in linear time

---

## Time and Space Complexity Explanation

### 1. Brute Force

For every starting index `i`, we scan all subarrays beginning there.

- Outer loop: `n` iterations
- Inner loop: up to `n` iterations
- Total: `O(n^2)`

Memory is constant because we do not store extra arrays.

### 2. Sliding Window

The window boundaries only move forward.

- `end` grows across the array
- `start` only grows as needed
- Each index enters and leaves the window at most once

Thus total work is `O(n)`.

Extra memory is constant: `O(1)`.

### 3. Prefix Sum + Hash Map

Each array element is processed once.

- We compute a running prefix sum
- We check the frequency of `prefix_sum - k`
- We update the map

So total time is `O(n)`.

We store previous prefix sums in a hash map, which may grow to `O(n)` entries in the worst case.

---

## Interview Questions to Practice

1. Why does the brute force solution take `O(n^2)` time?
2. When is the sliding window approach valid, and when does it fail?
3. Why does the sliding window require non-negative numbers?
4. What is the prefix sum formula for a subarray sum of `k`?
5. How does `prefix_sum - k` help us count subarrays?
6. What happens if the array contains negative numbers?
7. How would you modify the solution to count all subarrays instead of just checking existence?
8. What is the difference between checking existence and counting occurrences?
9. What are the edge cases?
   - empty array
   - all zeros
   - negative numbers
   - repeated values
   - `k = 0`
10. Could you explain why the hash map solution is linear time?

---

## Final Takeaway

- Brute force is easy to write but too slow.
- Sliding window is efficient for non-negative arrays.
- Prefix sum + hash map is the classic and most robust interview solution.

If the interview mentions negative numbers or wants the number of valid subarrays, prefer the prefix-sum + hash-map solution.

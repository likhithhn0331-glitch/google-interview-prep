# DSA PROBLEM 1 — Subarray Sum Equals K

## Problem Statement

Given an integer array `nums` and an integer `k`, return the number of contiguous subarrays whose sum equals `k`.

Example:

```python
nums = [1, 1, 1]
k = 2
# Output: 2
```

The subarrays that sum to `2` are:

- `[1, 1]` (from index 0 to 1)
- `[1, 1]` (from index 1 to 2)

## Key Insight: Prefix Sum + Hash Map

Let `prefix[i]` be the sum of the first `i` elements.

Then the sum of subarray `nums[i+1 ... j]` can be written as:

```text
prefix[j] - prefix[i] = k
```

This means:

- if the current prefix sum is `S`
- then we need a previous prefix sum of `S - k`

So the problem becomes: "How many times have we seen a prefix sum equal to `current_prefix_sum - k`?"

This is the central insight of the solution.

## Efficient Idea

Traverse the array while tracking:

- the running prefix sum
- a hash map of how many times each prefix sum has appeared so far

For each prefix sum `S`:

1. Check how many times `S - k` has appeared before.
2. Add that count to the answer.
3. Increment the count of current prefix sum `S`.

## Why This Works

If a previous prefix sum was `S - k`, then the subarray between that earlier point and the current index must sum to `k`.

Formally:

```text
sum(i+1 ... j) = prefix[j] - prefix[i] = k
```

Therefore, every time we encounter a prefix sum `S`, we count how many earlier prefix sums `S - k` were seen.

## Algorithm

```python
from collections import defaultdict


def subarray_sum_equals_k(nums, k):
    prefix_sum = 0
    count = 0
    seen = defaultdict(int)
    seen[0] = 1

    for num in nums:
        prefix_sum += num
        count += seen.get(prefix_sum - k, 0)
        seen[prefix_sum] += 1

    return count
```

## Complexity

- Time Complexity: `O(n)`
- Space Complexity: `O(n)` in the worst case

## Notes

This is a classic prefix-sum + hash-map problem and is one of the most important patterns in DSA interviews.

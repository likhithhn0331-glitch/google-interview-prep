# DSA PROBLEM 3 — Range Sum Query — Immutable

## Problem Statement

Given an integer array `nums`, implement a class `NumArray` that supports the following operations:

- `NumArray(nums)` initializes the object with the integer array `nums`.
- `sumRange(left, right)` returns the sum of the elements in `nums[left...right]`, inclusive.

The array is immutable after initialization, meaning you can preprocess it once and answer many queries efficiently.

Example:

```python
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0, 2))  # 1
print(obj.sumRange(2, 5))  # -1
print(obj.sumRange(0, 5))  # -3
```

## Key Insight: Prefix Sum Array

If we precompute a prefix sum array, then the sum of any subarray can be computed in constant time.

Let:

```text
prefix[0] = 0
prefix[i] = nums[0] + nums[1] + ... + nums[i-1]
```

Then the sum of `nums[left...right]` is:

```text
sum(left, right) = prefix[right + 1] - prefix[left]
```

This transforms each range-sum query into a simple subtraction.

## Efficient Idea

During initialization:

1. Create a prefix sum array of length `n + 1`.
2. Fill it so that each element stores the sum of all values up to that index.

Then for every query:

- compute `prefix[right + 1] - prefix[left]`
- return the result immediately

## Why This Works

The prefix sum array stores cumulative totals. The difference between two prefix sums tells us exactly how much was added between the two positions.

For example:

```text
nums = [1, 2, 3, 4]
prefix = [0, 1, 3, 6, 10]
```

Then:

```text
sum(1, 3) = prefix[4] - prefix[1] = 10 - 1 = 9
```

And indeed `nums[1] + nums[2] + nums[3] = 2 + 3 + 4 = 9`.

## Algorithm

```python
class NumArray:
    def __init__(self, nums):
        n = len(nums)
        self.prefix = [0] * (n + 1)
        for i in range(n):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
```

## Complexity

- Initialization: `O(n)`
- Each query: `O(1)`
- Extra space: `O(n)`

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^5 <= nums[i] <= 10^5`
- `0 <= left <= right < nums.length`
- At most `10^4` calls to `sumRange`

## Notes

This is a classic immutable prefix-sum problem. It is especially useful when the dataset is fixed and many range queries must be answered quickly.

Related problem: LeetCode 303 — Range Sum Query - Immutable.

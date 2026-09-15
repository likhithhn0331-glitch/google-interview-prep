# DSA PROBLEM 3 — Range Sum Query — Immutable

## Problem Restatement

Given an integer array `nums`, implement a class `NumArray` that supports:

- `NumArray(nums)` to initialize the data structure
- `sumRange(left, right)` to return the sum of elements from `left` to `right`, inclusive

The key constraint is that the array is immutable after initialization, so we can preprocess it once and handle many queries efficiently.

---

## Solution 1: Brute Force

### Idea

For each query, directly iterate through the elements from `left` to `right` and add them to a running total.

This is the simplest and most straightforward approach, and it works correctly for small inputs or a small number of queries.

### Algorithm

1. Start with `total = 0`
2. Loop from `left` to `right`
3. Add `nums[i]` to `total`
4. Return `total`

### Python Example

```python
class NumArray:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        total = 0
        for i in range(left, right + 1):
            total += self.nums[i]
        return total
```

### Why It Works

If a query asks for the sum of `nums[left...right]`, then adding each element one by one from that range gives the exact total.

### Strengths

- Very easy to understand
- Easy to implement correctly
- Good for tiny arrays and one-off queries

### Weaknesses

- Recomputes the same values repeatedly
- Slow for many queries

### Time and Space Complexity

- Initialization: `O(1)`
- Each query: `O(right - left + 1)`
- Total for `q` queries: `O(q * n)` in the worst case
- Extra space: `O(1)`

This approach is acceptable only when the number of queries is very small.

---

## Solution 2: Prefix Sum Array (Optimal)

### Idea

Precompute cumulative sums so that each range sum can be answered in constant time.

If `prefix[i]` is the sum of the first `i` elements, then:

```text
sum(nums[left...right]) = prefix[right + 1] - prefix[left]
```

This converts every query into a subtraction.

### Algorithm

1. Create a prefix array of size `n + 1`
2. Set `prefix[0] = 0`
3. For each index `i` from `0` to `n - 1`:
   - `prefix[i + 1] = prefix[i] + nums[i]`
4. To answer a query:
   - return `prefix[right + 1] - prefix[left]`

### Python Example

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

### Why It Works

The prefix sum array stores cumulative totals.

Example:

```text
nums = [1, 2, 3, 4]
prefix = [0, 1, 3, 6, 10]
```

Then:

```text
sum(1, 3) = prefix[4] - prefix[1] = 10 - 1 = 9
```

This matches the actual range sum:

```text
2 + 3 + 4 = 9
```

### Strengths

- Very fast query time
- Perfect for immutable data
- Great for many repeated queries

### Weaknesses

- Requires extra memory proportional to the array size
- If the array changes often, this structure becomes less useful unless rebuilt

### Time and Space Complexity

- Initialization: `O(n)`
- Each query: `O(1)`
- Total for `q` queries: `O(n + q)`
- Extra space: `O(n)`

This is the intended optimal solution for the immutable version of the problem.

---

## Comparison of Both Solutions

### Brute Force

- Good for understanding the problem
- Simple but inefficient
- Every query scans the range again
- Usable only for small arrays or low query volume

### Prefix Sum

- Best for repeated queries on a fixed array
- Preprocessing pays off when there are many range queries
- Query cost becomes constant time
- Naturally suited to the immutable constraint

### In one sentence

The brute force approach is simple but slow; the prefix-sum approach trades a one-time preprocessing cost for blazing-fast repeated queries.

---

## Time/Space Complexity Explanation

### 1. Brute Force

For a query `sumRange(left, right)`, we examine all elements from `left` to `right`.

- If the range length is `L = right - left + 1`, then the query takes `O(L)` time.
- In the worst case, `L = n`, so a single query is `O(n)`.
- If there are `q` queries, total cost becomes `O(q * n)`.
- Extra memory is constant: `O(1)`.

### 2. Prefix Sum

Initialization builds a cumulative array of size `n + 1`.

- Building the prefix sum array takes `O(n)` time.
- Each query subtracts two prefix values:
  - `prefix[right + 1] - prefix[left]`
  - This is `O(1)` per query.
- For `q` queries, total time is `O(n + q)`.
- Extra memory is `O(n)` because of the stored prefix sums.

### Why the Prefix Sum Wins

When many queries are asked against the same fixed array, the repeated scanning in the brute-force approach becomes expensive. The prefix sum reduces the repeated work to a single subtraction per query.

---

## Interview-Focused Discussion

### Core Idea to Emphasize

The problem is about turning repeated range queries into a constant-time lookup.

The phrase “immutable” is the key clue: because the array never changes, preprocessing is allowed and highly valuable.

### What Interviewers Often Want to Hear

- “I can preprocess once and answer queries faster.”
- “Use cumulative sums to convert subarray sums into prefix differences.”
- “For immutable data, prefix sums are the standard optimal design.”

---

## Interview Questions You Can Practice

1. What is the difference between a brute-force and a prefix-sum solution?
2. Why does the prefix-sum solution work only well when the array is immutable?
3. If the array were mutable and updated frequently, what other data structures might you consider?
4. How would you handle `sumRange` for millions of repeated queries?
5. Can this be solved with a segment tree or Fenwick tree? When would you choose them?
6. What happens if the array contains negative numbers?
7. Would the prefix-sum technique still work if the values were large or if there were very many queries?
8. What is the complexity trade-off between preprocessing and direct computation?
9. How would you adapt the solution to 1-indexed logic in a language like C++ or Java?
10. Can you explain the formula `prefix[right + 1] - prefix[left]` in plain English?

---

## Final Takeaway

For an immutable array, the prefix-sum approach is the correct interview solution. It reduces query time from potentially linear per query to constant time while keeping initialization efficient.

This is a classic example of using preprocessing to optimize repeated queries, and it is one of the most important patterns in DSA interviews.

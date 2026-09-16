# Longest Consecutive Sequence

## Problem

Given an unsorted array of integers `nums`, find the length of the longest consecutive elements sequence.

Example:

```python
nums = [100, 4, 200, 1, 3, 2]
```

The longest consecutive sequence is:

```python
[1, 2, 3, 4]
```

So the answer is:

```python
4
```

---

## 1) Brute Force Solution

### Idea

A simple way is to check every unique number in the array as a possible start of a sequence.

If a number `x` is the start of a sequence, then we keep increasing `x` by 1 as long as the next value exists in the array. We count how long the sequence is and keep the maximum value seen.

### Why it works

A sequence can only start at a number that has no previous value (`x - 1`) in the set. If `x - 1` exists, then `x` is not the beginning of a new chain, so we do not need to expand from it.

### Python Code

```python
# brute_force.py

def longest_consecutive_sequence_brute_force(nums):
    if not nums:
        return 0

    longest = 1
    unique_nums = set(nums)

    for num in unique_nums:
        if num - 1 not in unique_nums:
            current_length = 1
            while num + current_length in unique_nums:
                current_length += 1
            longest = max(longest, current_length)

    return longest
```

### Example Walkthrough

Input:

```python
nums = [100, 4, 200, 1, 3, 2]
```

Set of numbers:

```python
{100, 4, 200, 1, 3, 2}
```

Check `1`:
- `1 - 1 = 0` not present
- check `2`, `3`, `4` => sequence length = 4

Check `100` and `200`:
- both are isolated sequences of length 1

Final result: `4`

### Time Complexity

- Converting to a set: `O(n)`
- For each number, checking its sequence upward: worst-case `O(n^2)`
- Total: `O(n^2)` worst-case

### Space Complexity

- Set storage: `O(n)`

---

## 2) Hashing Interval-Based Solution

### Idea

Use a hash set to allow fast membership checks.

The key optimization is:
- only expand from the start of a sequence
- if `num - 1` is present, then this number is not the start, so skip it
- if `num - 1` is absent, then this number is the beginning of a sequence and we can count forward until no more adjacent values exist

This avoids checking the same sequence multiple times.

### Python Code

```python
# hashing_interval.py

def longest_consecutive_sequence_hashing_interval(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            current = num
            streak = 1
            while current + 1 in num_set:
                current += 1
                streak += 1
            longest = max(longest, streak)

    return longest
```

### Example Walkthrough

Input:

```python
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
```

Hash set:

```python
{0, 1, 2, 3, 4, 5, 6, 7, 8}
```

Start from `0`:
- `0 - 1 = -1` not present
- expand: `1, 2, 3, 4, 5, 6, 7, 8`
- length = 9

This gives the maximum result: `9`

### Time Complexity

- Building the set: `O(n)`
- Each sequence is expanded once from its start
- Total: `O(n)` average time

### Space Complexity

- Hash set: `O(n)`

---

## 3) Comparison of Both Solutions

### Brute Force

Pros:
- Very easy to understand
- Good for explaining the logic clearly
- Works correctly for small inputs

Cons:
- Repeatedly checks values from scratch
- Worst-case `O(n^2)` time
- Not efficient for large arrays

### Hashing Interval-Based

Pros:
- Much faster on large inputs
- Uses constant-time set lookups
- Only expands sequences from their start
- Average complexity: `O(n)`

Cons:
- Slightly more advanced logic
- Requires understanding of hash sets and sequence boundaries

### Summary

| Approach | Time Complexity | Space Complexity | Best For |
|----------|-----------------|------------------|----------|
| Brute Force | `O(n^2)` | `O(n)` | Small inputs, teaching clarity |
| Hashing Interval | `O(n)` | `O(n)` | Real interview solutions and large datasets |

---

## 4) Why the Hashing Solution Is Better

The important optimization is this:

- We do not check every number as a possible start
- We only start counting when `num - 1` is missing
- That means every valid sequence is expanded only once

This reduces repeated work dramatically.

In a large array, repeated upward expansions can become expensive. The set-based solution avoids that by making membership tests fast and by skipping redundant checks.

---

## 5) Interview Questions and Answers

### Q1. What is the main idea behind the brute-force solution?

Answer:

For every number that is not preceded by `num - 1`, we treat it as the start of a sequence and count upward until the next value is missing. We maintain the longest streak found.

---

### Q2. Why is the brute-force solution not ideal for large input sizes?

Answer:

Because every number may trigger a scan across many values, resulting in worst-case quadratic time complexity. For example, if the input is large and mostly consecutive, each number may repeatedly walk through a long sequence.

---

### Q3. What is the key optimization in the hashing solution?

Answer:

Only expand from a number if `num - 1` is not present in the set. That ensures we only start counting at the beginning of each chain, avoiding repeated work.

---

### Q4. Why does using a set help?

Answer:

A set allows constant-time membership checks (`x in set`) on average. This makes it efficient to test whether a value belongs to the array and whether a sequence can continue.

---

### Q5. What is the time complexity of the hashing solution?

Answer:

Average time complexity is `O(n)`, because:
- creating the set is `O(n)`
- each number is processed a constant number of times
- each sequence is expanded once from its start

---

### Q6. Does the solution work with duplicates?

Answer:

Yes. Duplicate values are ignored because we use a set, so duplicates do not create extra sequence length.

Example:

```python
nums = [1, 1, 2, 2, 3, 3]
```

The set becomes:

```python
{1, 2, 3}
```

The longest consecutive sequence length is `3`.

---

### Q7. Does the sequence need to appear contiguously in the original array?

Answer:

No. The values only need to exist in the array as a set of numbers. Their positions in the original array do not matter.

Example:

```python
nums = [100, 4, 200, 1, 3, 2]
```

Even though the values are spread out, they still form the consecutive sequence `[1, 2, 3, 4]`.

---

### Q8. What is the space complexity of the hashing solution?

Answer:

It is `O(n)` because the set stores all unique values from the input.

---

### Q9. Can the brute-force solution still be useful in interviews?

Answer:

Yes, as a starting point to explain the logic and validate correctness. It is easy to reason about, and it helps show the key insight that we only need to examine sequence starts.

---

### Q10. What would be the best final interview answer?

Answer:

Use the hash-set solution:
- convert the nums array to a set
- iterate through each number
- if `num - 1` is missing, expand upward from `num`
- track the maximum length

This gives average `O(n)` time and `O(n)` space, which is optimal for this problem.

---

## Final Takeaway

The core insight is that only the start of a consecutive run matters.

If a number has a predecessor in the set, it is not the start of a new sequence. If it does not, then it can begin a run, and we count forward until the sequence ends.

This leads to the efficient `O(n)` hashing solution, which is the standard interview-ready answer.

# Longest Consecutive Sequence

## 1. Problem

Given an unsorted array of integers `nums`, find the length of the longest consecutive elements sequence.

Example:

```python
nums = [100, 4, 200, 1, 3, 2]
```

Longest consecutive sequence:

```python
[1, 2, 3, 4]
```

Answer:

```python
4
```

The sequence does not need to be contiguous in the original array. Only the values matter.

---

## 2. Pattern

This problem fits the pattern:

- Hash set / value lookup optimization
- Sequence detection using boundaries
- Only expand from sequence starts

The key idea is to check whether a value is the beginning of a run by testing whether `value - 1` exists.

---

## 3. Recognition Clues

This problem is likely when you see:

- "unsorted array"
- "consecutive numbers"
- "find longest run of integers"
- "values may be anywhere in the array"
- "need length only, not the actual sequence"

These clues suggest that sorting is possible but not ideal, and set-based checking is the better route.

---

## 4. Brute Force

A naive way:

- Take each unique value as a possible start
- Check forward while the next number exists
- Track the longest run

Pseudo-code:

```python
longest = 0
seen = set(nums)

for x in seen:
    if x - 1 not in seen:
        length = 1
        while x + 1 in seen:
            x += 1
            length += 1
        longest = max(longest, length)
```

This is already close to the optimized solution, but the brute-force version can be interpreted as checking all values repeatedly without the optimization that only starts from valid sequence starters.

---

## 5. Brute-force Complexity

If we check every value and scan forward from each one:

- Worst-case time: `O(n^2)`
- Space: `O(n)` for the set or hash structure

This is acceptable for educational purposes but too slow for large arrays.

---

## 6. Optimized Intuition

The main optimization is:

- If `num - 1` exists, then `num` is not the start of a new consecutive sequence.
- If `num - 1` does not exist, then `num` must be the beginning of a sequence.

That means each sequence is only expanded once from its true start.

This avoids redundant counting and gives linear performance on average.

---

## 7. Invariant

At every step while expanding from a sequence start:

- `current` is the latest number in the currently explored run
- all numbers from the start up to `current` are present in the set
- the run length is accurate for that sequence

When the next number is missing, we stop and record the streak length.

---

## 8. Algorithm

1. Convert the array to a set to remove duplicates and allow fast lookup.
2. Iterate through each unique value.
3. If `num - 1` is not in the set, this is the start of a sequence.
4. Count upward while `current + 1` is in the set.
5. Track the longest streak seen.
6. Return the maximum length.

Python version:

```python
def longest_consecutive_sequence(nums):
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

---

## 9. Complexity

### Time Complexity

- Building the set: `O(n)`
- Iterating over unique numbers: `O(n)`
- Each valid sequence is expanded only once:
  - total is still `O(n)` in average case

Overall average:

```python
O(n)
```

Worst-case for hash operations is still close to linear average in Python sets, so the practical complexity is `O(n)`.

### Space Complexity

- The set stores all unique values: `O(n)`

Overall:

```python
O(n)
```

---

## 10. Edge Cases

- Empty array
  ```python
  [] -> 0
  ```

- Single element
  ```python
  [1] -> 1
  ```

- All duplicates
  ```python
  [5, 5, 5] -> 1
  ```

- Negative numbers
  ```python
  [-2, -1, 0, 1, 3, 4] -> 4
  ```

- Sequence spread across array
  ```python
  [100, 4, 200, 1, 3, 2] -> 4
  ```

- Already sorted array
  ```python
  [1, 2, 3, 4, 5] -> 5
  ```

---

## 11. Common Mistakes

1. Counting from every number instead of only sequence starts
   - leads to repeated work

2. Forgetting to remove duplicates
   - duplicates should not increase the length

3. Checking `num + 1` instead of `num - 1` when deciding sequence starts
   - this can break the logic

4. Not handling empty input
   - return `0` for `[]`

5. Assuming the sequence must be adjacent in the original array
   - it does not; only the values matter

6. Not considering negatives
   - the logic still works with negative numbers

---

## 12. Alternative Approach

### Sorting Approach

Another accepted method is:

1. Sort the array
2. Traverse and count consecutive runs
3. Reset count when the difference is not 1

Example:

```python
def longest_consecutive_sequence_sort(nums):
    if not nums:
        return 0

    nums.sort()
    longest = 1
    current = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue
        if nums[i] == nums[i - 1] + 1:
            current += 1
        else:
            current = 1
        longest = max(longest, current)

    return longest
```

### Complexity

- Sorting: `O(n log n)`
- Traversal: `O(n)`
- Total: `O(n log n)`

This works, but the hash-set approach is better for interview performance.

---

## 13. Google Follow-ups

### Follow-up 1: What if the array is huge?

Use the hash-set solution. It is the preferred approach because it avoids sorting and keeps average time linear.

### Follow-up 2: Can we do it in place without extra memory?

Not efficiently in the general case. To do fast membership checks, a set is the standard tool. Sorting also uses memory in practice and still takes `O(n log n)`.

### Follow-up 3: What if there are duplicates?

Use a set to deduplicate. Since duplicates do not change the length of a consecutive run, they should not be counted multiple times.

### Follow-up 4: What if the numbers are negative or zero?

The same logic works because we only compare against `num - 1` and `num + 1`.

### Follow-up 5: Why not sort the array first?

Sorting is valid, but it gives `O(n log n)` time, which is slower than the hash-based approach. For interview optimization questions, the set-based method is usually better.

### Follow-up 6: Could we solve it with a dictionary or map?

Yes, a set is effectively a map with only membership. The optimization depends on constant-time lookup, not on the exact data structure.

### Follow-up 7: Why does only checking sequence starts matter?

Because any number that already has a predecessor is guaranteed to belong to a sequence that was or will be counted from its smaller start. We avoid repeated counting by ignoring those values.

---

## Interview Summary

Best answer to give in an interview:

- Use a hash set
- Only expand from numbers whose predecessor does not exist
- Count consecutive values from there
- Track the maximum run length

This gives:

- Time: `O(n)` average
- Space: `O(n)`

It is the standard optimal solution for this problem.

# Merge Intervals - Notes

## 1) Problem

Given a list of intervals, merge all overlapping intervals and return a list of non-overlapping intervals that cover the same range.

Example:

```python
intervals = [
    [1, 3],
    [2, 6],
    [8, 10],
    [9, 12]
]
```

Output:

```python
[[1, 6], [8, 12]]
```

Rule:
- If intervals touch at a boundary, they are considered overlapping for this problem.
- Example: `[1, 3]` and `[3, 5]` -> `[1, 5]`

---

## 2) Pattern

This is an interval pattern problem.

Common signals:
- ranges
- start/end pairs
- overlapping segments
- schedules / time windows
- occupied vs free periods

Pattern name:

```text
Intervals
```

Core idea:

```text
Sort by start
Scan left to right
Merge when overlap exists
```

---

## 3) Recognition Clues

Ask yourself:
- Are we dealing with ranges or time segments?
- Do we need to merge or compress overlapping spans?
- Are intervals unordered or arbitrary?
- Do boundaries like `end == next_start` count as overlap?

If yes, think:

```text
MERGE INTERVALS
```

The typical first move is:

```text
Sort by start time
```

---

## 4) Brute Force

A brute force approach would compare every interval with every other interval to determine overlaps, then merge them incrementally.

Pseudo:

```python
for each interval i:
    for each interval j after i:
        if intervals overlap:
            merge them
```

This works, but it is inefficient.

---

## 5) Brute-force Complexity

Let `n` be the number of intervals.

- comparing all pairs: `O(n^2)`
- merging may add more work depending on implementation

Total:

```text
Time: O(n^2)
Space: O(n)
```

This is acceptable for tiny inputs but not for large intervals.

---

## 6) Optimized Intuition

After sorting by start time, the key insight is:

> Once intervals are ordered, only the current merged interval matters.

This means we do not need to compare every interval against every previous interval.

We just compare the next interval to the last merged interval.

---

## 7) Invariant

Important invariant:

```text
After processing the first k sorted intervals,
merged[-1] represents the complete merged output for the active overlapping group.
```

This is the heart of the solution.

If the next interval starts before or at the current merged end, then it overlaps and should extend the current merged range.

---

## 8) Algorithm

### Standard greedy algorithm

```python
def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0][:]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged
```

### Why it works

- Sorting ensures earlier starts come first.
- If `start <= last_end`, overlap exists.
- Merge by extending the last interval's end.
- If `start > last_end`, no overlap: finalize and begin a new interval.

---

## 9) Complexity

Let `n` = number of intervals.

### Standard approach

- sorting: `O(n log n)`
- single left-to-right scan: `O(n)`

Total:

```text
Time: O(n log n)
Space: O(n)
```

This is the optimal standard solution for interval merging.

---

## 10) Edge Cases

Consider these carefully:

1. Empty input
   ```python
   [] -> []
   ```

2. Single interval
   ```python
   [[1, 5]] -> [[1, 5]]
   ```

3. Already sorted input
   ```python
   [[1, 3], [2, 6], [8, 10]]
   ```

4. Unsorted input
   ```python
   [[8, 10], [1, 3], [2, 6]]
   ```

5. Nested intervals
   ```python
   [[1, 10], [2, 5]] -> [[1, 10]]
   ```

6. Boundary-touching intervals
   ```python
   [[1, 3], [3, 5]] -> [[1, 5]]
   ```

7. Completely separate intervals
   ```python
   [[1, 2], [4, 5], [7, 9]]
   ```

8. Reversed bounds
   ```python
   [[9, 4], [2, 8]]
   ```
   Normalize to `[4, 9]` and `[2, 8]` before merging.

---

## 11) Common Mistakes

1. Comparing with the wrong interval
   - always compare current interval vs the last merged interval

2. Using strict `<` instead of `<=`
   - if intervals touch at the endpoint, they overlap

3. Forgetting to sort
   - the greedy strategy depends on sorted order

4. Not normalizing reversed endpoints
   - `[9, 4]` should be treated as `[4, 9]`

5. Updating the wrong interval
   - ensure you extend `merged[-1][1]`, not the current one

6. Not handling empty arrays
   - return `[]` immediately

7. Assuming intervals are always valid
   - some inputs may not be sorted or may have reversed bounds

---

## 12) Alternative Approach

A less efficient but intuitive alternative is to treat coverage as a set of points on a number line.

Idea:
- add every integer point from all intervals into a set
- sort the points
- compress consecutive values into ranges

Example:

```python
[[1, 3], [2, 6]]
```

Covered points:

```python
{1, 2, 3, 4, 5, 6}
```

Merged output:

```python
[[1, 6]]
```

This works, but it is usually slower and uses more memory when ranges are large.

---

## 13) Google Follow-ups

### Follow-up 1: What if intervals are given in a stream and cannot be sorted first?

Answer:
- If the input truly arrives as a stream and we cannot store all intervals, then the full standard merge solution is harder.
- Usually we store intervals until processing, then sort them.
- If sorted streaming is required, custom data structures or external sorting are needed.

---

### Follow-up 2: Can the algorithm be modified for half-open intervals `[start, end)`?

Answer:
- Yes, the overlap condition changes slightly.
- For half-open intervals, two intervals overlap if `next_start < current_end` when endpoints are treated as exclusive.
- The interpretation depends on interval semantics.

---

### Follow-up 3: What if the input is very large?

Answer:
- The standard `O(n log n)` solution remains the right choice.
- Avoid point-by-point set coverage because it can explode in memory if ranges are large.

---

### Follow-up 4: What if there are duplicate intervals?

Answer:
- Duplicates are naturally handled by the merge logic.
- Example: `[1, 3]` and `[1, 3]` -> `[1, 3]`

---

### Follow-up 5: Can we do this in place without extra memory?

Answer:
- We can sort the list in place and maintain a result array.
- The output itself is still required, so some extra space is inevitable if we return a new list.

---

### Follow-up 6: What happens with negative numbers?

Answer:
- The algorithm still works exactly the same.
- Sorting handles negative numbers naturally.

---

### Follow-up 7: Is this a greedy problem?

Answer:
- Yes, it is a classic greedy interval problem.
- The greedy choice is to always extend the current merged interval whenever the next interval overlaps it.

---

### Follow-up 8: Why not use a hash map for this?

Answer:
- A hash map is not the natural fit for interval merging because the important relationship is based on ordering and overlap, not unique keys.
- The sorting + scan method is simpler and more direct.

---

## Quick Summary

```text
Problem: merge overlapping intervals
Pattern: Intervals
Recognition: ranges / start-end pairs / overlap
Core idea: sort + greedy scan
Invariant: current merged interval is the active overlap group
Time: O(n log n)
Space: O(n)
```

This is one of the most common interval interview problems and is usually solved with the sorted greedy scan.

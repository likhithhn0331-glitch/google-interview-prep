# Merge Intervals

## Problem Summary

Given an array of intervals, merge all overlapping intervals and return the sorted list of non-overlapping merged intervals.

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
[
    [1, 6],
    [8, 12]
]
```

Important rule:
- Intervals that touch at a boundary are treated as overlapping in the standard Merge Intervals problem.
- Example: `[1, 3]` and `[3, 5]` merge into `[1, 5]`.

---

## 1) Brute Force Solution

File: `brute_force.py`

### Idea

A straightforward way is:
- normalize each interval so bounds are ordered (`[start, end]` with `start <= end`)
- sort the intervals by start time
- scan through them one by one
- compare the current interval with the last merged interval
- if they overlap, expand the last merged interval
- otherwise, add the current interval as a new merged interval

### Python Code

```python
def merge_intervals_brute_force(intervals):
    if not intervals:
        return []

    normalized = []
    for start, end in intervals:
        if start > end:
            start, end = end, start
        normalized.append([start, end])

    normalized.sort(key=lambda interval: (interval[0], interval[1]))

    merged = []
    for current in normalized:
        if not merged:
            merged.append(current[:])
            continue

        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current[:])

    return merged
```

### Why this works

After sorting, intervals with earlier starts appear first.

For the current interval and the last merged interval:
- if `current_start <= last_end`, they overlap
- merge by setting `last_end = max(last_end, current_end)`
- if `current_start > last_end`, they do not overlap, so start a new merged interval

This maintains the invariant that `merged[-1]` is always the merged range for the current active group of overlapping intervals.

### Example Walkthrough

Input:

```python
[[1, 3], [2, 6], [8, 10], [9, 12]]
```

Sorted:

```python
[[1, 3], [2, 6], [8, 10], [9, 12]]
```

Process:
- `[1, 3]` → start merged list
- `[2, 6]` overlaps `[1, 3]` → merge to `[1, 6]`
- `[8, 10]` does not overlap `[1, 6]` → start new interval
- `[9, 12]` overlaps `[8, 10]` → merge to `[8, 12]`

Final:

```python
[[1, 6], [8, 12]]
```

---

## 2) Hashing Interval-Based Solution

File: `hashing_interval.py`

### Idea

This alternative approaches the problem by thinking in terms of all integer points covered by the intervals.

- collect every covered integer value from all intervals into a set
- sort the set
- group consecutive numbers into ranges
- every contiguous block becomes one merged interval

This is a valid hash-based coverage strategy.

### Python Code

```python
def merge_intervals_hashing_interval(intervals):
    if not intervals:
        return []

    covered = set()
    for start, end in intervals:
        if start > end:
            start, end = end, start
        for value in range(start, end + 1):
            covered.add(value)

    if not covered:
        return []

    points = sorted(covered)
    merged = []
    start = points[0]
    prev = points[0]

    for value in points[1:]:
        if value == prev + 1:
            prev = value
            continue

        merged.append([start, prev])
        start = prev = value

    merged.append([start, prev])
    return merged
```

### Why this works

If a value is covered by any input interval, it enters the set.

Once all covered points are collected:
- consecutive integers represent a continuous covered segment
- a break in consecutive values means the current merged interval should end
- the next consecutive block starts a new interval

### Example Walkthrough

Input:

```python
[[1, 3], [2, 6], [8, 10], [9, 12]]
```

Covered points:

```python
{1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12}
```

Consecutive groups:
- `[1, 6]`
- `[8, 12]`

Final:

```python
[[1, 6], [8, 12]]
```

---

## 3) Comparison of Both Solutions

### Brute Force / Greedy Scan

Strengths:
- simple and easy to explain
- optimal for many interview questions on intervals
- very efficient in practice for moderate input sizes
- works directly on interval boundaries

Weaknesses:
- not the fastest when intervals are huge and spread over large ranges
- still requires a sort, which costs `O(n log n)`

### Hashing Interval Coverage

Strengths:
- conceptually very clear: mark all covered points, then compress them
- easy to reason about when the problem is about coverage over a number line
- good for teaching the idea of “covered points and contiguous ranges”

Weaknesses:
- can be extremely expensive if the interval values are far apart or large
- if intervals cover a huge numeric range, storing all covered values becomes costly
- not the standard or recommended solution for interval problems in interviews

### Which one is preferred?

For interview problems, the standard answer is the greedy sorted-scan solution:
- sort by start
- maintain current merged interval
- compare next interval's start against current end

This is the classic interval pattern and is the best choice for production-quality code.

The hashing-based approach is useful as an alternative way to think about coverage, but it is usually not the most efficient or elegant solution for large interval ranges.

---

## 4) Time and Space Complexity

Let `n` be the number of intervals.

### Brute Force / Greedy Sort-and-Scan

Time complexity:
- sorting the intervals: `O(n log n)`
- single scan through sorted intervals: `O(n)`
- total: `O(n log n)`

Space complexity:
- extra space for the merged result: `O(n)` in the worst case
- input normalization adds a small extra structure when needed

Overall:

```text
Time:  O(n log n)
Space: O(n)
```

### Hashing Interval Coverage

Time complexity:
- add all covered points to a set: depends on total covered integer range size
- sorting the set: `O(m log m)` where `m` is the number of covered integer points
- total is roughly `O(R log R)` for a covered range size `R`

If intervals span a large numeric range, this can be much worse than `O(n log n)`.

Space complexity:
- storing all covered points in a set: `O(m)`

Overall:

```text
Time:  O(R log R) in the covered-value model
Space: O(R)
```

where `R` is the number of distinct integer points covered by the intervals.

### Key lesson

The greedy interval approach is better when intervals are given as ranges, because it works on interval boundaries rather than all integer points between them.

---

## 5) Why Sorting Is the Core Observation

The most important insight in this problem is:

> Once intervals are sorted by their start values, each interval only needs to be compared with the current merged interval.

This works because:
- all later intervals begin at or after the current interval's start
- only the current merged interval matters for overlap checks
- if two intervals do not overlap, we can safely finalize the current merged interval and start a new one

That is why the standard solution is:

```text
Sort by start
Scan left to right
Merge when needed
```

---

## 6) Interview Questions and Answers

### Q1: What is the standard approach to this problem?

Answer:

Sort the intervals by start time and scan left to right. Maintain the current merged interval. If the next interval overlaps the current one, extend the current interval. Otherwise, finalize the current interval and start a new one.

---

### Q2: How do you detect overlap between intervals?

Answer:

If the intervals are sorted by start, and we have a current merged interval `[current_start, current_end]`, then the next interval `[next_start, next_end]` overlaps when:

```python
next_start <= current_end
```

This is the standard condition for interval overlap in Merge Intervals.

---

### Q3: What if intervals touch at a boundary like `[1, 3]` and `[3, 5]`?

Answer:

They are considered overlapping in this problem, so the correct merged result is `[1, 5]`.

The condition is `next_start <= current_end`, not `next_start < current_end`.

---

### Q4: Why is sorting necessary?

Answer:

Without sorting, it is hard to know whether a new interval belongs to the currently active merged group or should start a new group. Sorting by start ensures that only local comparisons are needed.

---

### Q5: What is the time complexity of the standard solution?

Answer:

```text
O(n log n)
```

because sorting dominates the runtime. The final scan is linear.

---

### Q6: What is the space complexity of the standard solution?

Answer:

```text
O(n)
```

in the worst case, because the output itself can contain up to `n` intervals.

---

### Q7: Could there be an easier hash-based solution?

Answer:

Yes, you could mark every integer point covered by all intervals in a set and then compress consecutive values into ranges. It works logically, but it is generally less efficient because it depends on the size of the covered numeric range.

---

### Q8: Does the algorithm handle unsorted input?

Answer:

Yes. The standard interval solution sorts input first, so it works even if the original intervals arrive in arbitrary order.

---

### Q9: What happens if one interval contains another?

Answer:

No problem. Example: `[1, 10]` and `[2, 5]`.

The second interval is completely inside the first, so they overlap. The merged interval remains `[1, 10]`.

---

### Q10: What if intervals are completely separate?

Answer:

Then they never overlap and they remain separate in the output.

Example:

```python
[[1, 2], [4, 5], [7, 9]]
```

Output:

```python
[[1, 2], [4, 5], [7, 9]]
```

---

## 7) Final Interview Summary

The classic merge-interval solution is:

```python
intervals.sort(key=lambda x: x[0])
merged = []

for start, end in intervals:
    if not merged or start > merged[-1][1]:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)
```

This is the most common and efficient interview answer.

The hashing-based version is a useful alternative for understanding coverage, but it is less optimal when intervals cover a large numeric range.

---

## 8) Recommended Final Code (Standard Solution)

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

This is the standard solution pattern most interviewers expect.

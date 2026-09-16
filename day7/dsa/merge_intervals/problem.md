# Merge Intervals

## Problem Statement

Given an array of intervals where each interval is represented by a pair
of integers:

``` text
[start, end]
```

merge all overlapping intervals and return an array containing the
non-overlapping intervals that cover all the intervals in the original
input.

An interval represents a continuous range from its `start` value to its
`end` value.

Two intervals overlap when their ranges have a common portion, including
the boundary when one interval starts exactly where another interval
ends.

For example:

``` text
[1, 3]
[2, 6]
```

overlap because the second interval begins before the first interval
ends.

They can therefore be merged into:

``` text
[1, 6]
```

------------------------------------------------------------------------

## Formal Input

You are given:

``` text
intervals: an array/list of intervals
```

Each interval contains two values:

``` text
[start, end]
```

For example:

``` text
intervals = [
    [1, 3],
    [2, 6],
    [8, 10],
    [9, 12]
]
```

The input intervals may:

-   appear in arbitrary order,
-   overlap partially,
-   overlap completely,
-   be contained inside another interval,
-   touch at a boundary,
-   or be completely separate.

------------------------------------------------------------------------

## Expected Output

Return a collection of intervals such that:

1.  Every point covered by an input interval remains covered.
2.  All overlapping intervals have been merged.
3.  No two intervals in the output overlap.
4.  The resulting intervals collectively represent the same covered
    ranges as the original intervals.

For:

``` text
[
    [1, 3],
    [2, 6],
    [8, 10],
    [9, 12]
]
```

the result is:

``` text
[
    [1, 6],
    [8, 12]
]
```

The output contains non-overlapping intervals.

------------------------------------------------------------------------

# Understanding an Interval

An interval:

``` text
[start, end]
```

represents a range beginning at:

``` text
start
```

and ending at:

``` text
end
```

For example:

``` text
[2, 5]
```

represents the range:

``` text
2 ───────── 5
```

Another interval:

``` text
[4, 8]
```

represents:

``` text
4 ───────────── 8
```

Because these ranges overlap between `4` and `5`, they can be merged.

The merged interval is:

``` text
[2, 8]
```

------------------------------------------------------------------------

# What Does "Overlap" Mean?

Suppose we have two intervals:

``` text
[a, b]
[c, d]
```

assuming:

``` text
a <= b
c <= d
```

If the intervals are ordered by their starting points such that:

``` text
a <= c
```

then the intervals overlap when:

``` text
c <= b
```

For example:

``` text
[1, 5]
[3, 7]
```

Since:

``` text
3 <= 5
```

they overlap.

The merged interval is:

``` text
[1, 7]
```

------------------------------------------------------------------------

# Boundary-Touching Intervals

Consider:

``` text
[1, 3]
[3, 5]
```

The intervals touch at:

``` text
3
```

For the standard Merge Intervals problem, these intervals are treated as
overlapping and can be merged:

``` text
[1, 5]
```

Therefore, when comparing:

``` text
current_end
```

with:

``` text
next_start
```

the condition is commonly:

``` text
next_start <= current_end
```

not:

``` text
next_start < current_end
```

Always follow the exact interval semantics specified by the problem.

------------------------------------------------------------------------

# Example 1

## Input

``` text
intervals = [
    [1, 3],
    [2, 6],
    [8, 10],
    [9, 12]
]
```

## Step 1 --- Sort by Start

The intervals are already ordered:

``` text
[1, 3]
[2, 6]
[8, 10]
[9, 12]
```

## Step 2 --- Compare the First Two

Current:

``` text
[1, 3]
```

Next:

``` text
[2, 6]
```

Since:

``` text
2 <= 3
```

they overlap.

Merge them:

``` text
[1, 6]
```

## Step 3 --- Compare with `[8, 10]`

Current:

``` text
[1, 6]
```

Next:

``` text
[8, 10]
```

Since:

``` text
8 > 6
```

they do not overlap.

Therefore:

``` text
[1, 6]
```

is complete.

Start a new current interval:

``` text
[8, 10]
```

## Step 4 --- Compare with `[9, 12]`

Current:

``` text
[8, 10]
```

Next:

``` text
[9, 12]
```

Since:

``` text
9 <= 10
```

they overlap.

Merge:

``` text
[8, 12]
```

## Final Output

``` text
[
    [1, 6],
    [8, 12]
]
```

------------------------------------------------------------------------

# Example 2 --- Unsorted Input

## Input

``` text
[
    [8, 10],
    [1, 3],
    [2, 6],
    [9, 12]
]
```

The input is not sorted.

First sort by the starting value:

``` text
[
    [1, 3],
    [2, 6],
    [8, 10],
    [9, 12]
]
```

Then merge:

``` text
[1, 3] + [2, 6]
→ [1, 6]

[8, 10] + [9, 12]
→ [8, 12]
```

Final result:

``` text
[
    [1, 6],
    [8, 12]
]
```

------------------------------------------------------------------------

# Example 3 --- Completely Separate Intervals

## Input

``` text
[
    [1, 2],
    [4, 5],
    [7, 9]
]
```

No intervals overlap.

Therefore the output remains:

``` text
[
    [1, 2],
    [4, 5],
    [7, 9]
]
```

------------------------------------------------------------------------

# Example 4 --- One Interval Completely Contains Another

## Input

``` text
[
    [1, 10],
    [2, 5]
]
```

The second interval is completely inside the first.

They overlap.

The merged result remains:

``` text
[1, 10]
```

The algorithm must not accidentally shrink the current interval.

------------------------------------------------------------------------

# Example 5 --- Multiple Nested Intervals

## Input

``` text
[
    [1, 10],
    [2, 5],
    [3, 7],
    [4, 9]
]
```

All intervals are contained within or overlap:

``` text
[1, 10]
```

Therefore:

``` text
[
    [1, 10]
]
```

------------------------------------------------------------------------

# Example 6 --- Boundary Touching

## Input

``` text
[
    [1, 3],
    [3, 5]
]
```

They touch at `3`.

Under the standard Merge Intervals interpretation, they merge into:

``` text
[
    [1, 5]
]
```

------------------------------------------------------------------------

# Example 7 --- Single Interval

## Input

``` text
[
    [1, 5]
]
```

There is nothing to merge.

Output:

``` text
[
    [1, 5]
]
```

------------------------------------------------------------------------

# Example 8 --- Empty Input

## Input

``` text
[]
```

There are no intervals.

Output:

``` text
[]
```

------------------------------------------------------------------------

# Pattern Classification

This problem belongs to the:

``` text
Intervals
```

pattern.

The common solution pattern is:

``` text
Sort by Start
       ↓
Scan from Left to Right
       ↓
Maintain Current Interval
       ↓
Check Overlap
       ↓
Merge OR Finalize
```

More specifically:

``` text
Sorting + Greedy Interval Merging
```

------------------------------------------------------------------------

# Core Pattern Recognition Clue

When you see a problem involving:

-   ranges,
-   time intervals,
-   start/end pairs,
-   overlapping segments,
-   merging schedules,
-   occupied/free periods,

you should immediately consider:

``` text
INTERVAL PATTERN
```

For the basic Merge Intervals problem, the next thought should be:

``` text
Sort by start time
```

Then perform a linear scan.

------------------------------------------------------------------------

# Why Do We Sort?

Sorting is the key observation.

Suppose the intervals are:

``` text
[8, 10]
[1, 3]
[2, 6]
[9, 12]
```

Without sorting, relationships between intervals are difficult to reason
about.

After sorting:

``` text
[1, 3]
[2, 6]
[8, 10]
[9, 12]
```

we know that every interval we encounter later starts at or after the
current interval's start.

This gives us a powerful invariant:

> Once intervals are sorted by starting point, we only need to compare
> the next interval with the currently merged interval.

------------------------------------------------------------------------

# The Central Invariant

The most important interview concept in Merge Intervals is the
invariant.

After processing the first `i` sorted intervals:

> The current interval represents the complete merged range of all
> overlapping intervals encountered so far that belong to the current
> group.

For example:

``` text
[1, 3]
[2, 6]
[4, 8]
```

After processing the first two:

``` text
current = [1, 6]
```

After processing `[4, 8]`:

``` text
current = [1, 8]
```

The current interval always represents the complete merged coverage of
the active overlapping group.

------------------------------------------------------------------------

# How Do We Determine Overlap?

Suppose the current merged interval is:

``` text
[current_start, current_end]
```

and the next sorted interval is:

``` text
[next_start, next_end]
```

Because the intervals are sorted by start:

``` text
next_start >= current_start
```

Therefore, overlap depends on whether:

``` text
next_start <= current_end
```

If:

``` text
next_start <= current_end
```

then the intervals overlap.

If:

``` text
next_start > current_end
```

then they do not overlap.

------------------------------------------------------------------------

# How Do We Merge?

If the intervals overlap:

``` text
[current_start, current_end]
[next_start, next_end]
```

the merged interval becomes:

``` text
[
    current_start,
    max(current_end, next_end)
]
```

Why?

The merged interval starts at:

``` text
current_start
```

because the intervals are sorted by start.

The merged interval ends at whichever interval extends farther:

``` text
max(current_end, next_end)
```

------------------------------------------------------------------------

# Important Example

Consider:

``` text
current = [1, 10]
next    = [2, 5]
```

They overlap.

A common mistake is to set:

``` text
end = 5
```

That would incorrectly shrink the range.

Instead:

``` text
max(10, 5) = 10
```

so:

``` text
merged = [1, 10]
```

This is why the `max` operation is essential.

------------------------------------------------------------------------

# Non-Overlapping Case

Suppose:

``` text
current = [1, 6]
next    = [8, 10]
```

Since:

``` text
8 > 6
```

there is no overlap.

Therefore:

``` text
[1, 6]
```

is finalized.

Then:

``` text
current = [8, 10]
```

and scanning continues.

------------------------------------------------------------------------

# Conceptual Algorithm

The algorithm can be described without code as follows:

``` text
1. If the input is empty, return an empty result.
2. Sort intervals by their start value.
3. Treat the first interval as the current merged interval.
4. Process each remaining interval.
5. If the next interval overlaps the current interval:
       extend the current interval's end if necessary.
6. Otherwise:
       add the current interval to the result.
       start a new current interval.
7. Add the final current interval to the result.
8. Return the result.
```

------------------------------------------------------------------------

# Pseudocode

``` text
if intervals is empty:
    return []

sort intervals by start

current = first interval
result = []

for next_interval in remaining intervals:

    if next_interval.start <= current.end:

        current.end =
            max(current.end, next_interval.end)

    else:

        add current to result
        current = next_interval

add current to result

return result
```

This is the algorithmic structure you should understand before
implementing it.

------------------------------------------------------------------------

# Complexity

Let:

``` text
n = number of intervals
```

## Sorting

Sorting the intervals requires:

``` text
O(n log n)
```

time.

## Scan

After sorting, the intervals are scanned once:

``` text
O(n)
```

time.

Therefore:

``` text
O(n log n) + O(n)
```

which simplifies to:

``` text
O(n log n)
```

overall time.

------------------------------------------------------------------------

# Space Complexity

The space complexity depends on the implementation and the sorting
method used.

The result itself can contain up to:

``` text
O(n)
```

intervals.

Therefore the output requires:

``` text
O(n)
```

space in the worst case.

Additional auxiliary space depends on the programming language and
sorting implementation.

When discussing complexity in an interview, distinguish:

``` text
Output space
```

from:

``` text
Auxiliary space
```

rather than automatically combining them.

------------------------------------------------------------------------

# Why This Is a Greedy Algorithm

Merge Intervals can be viewed as a greedy scan.

At every step, once intervals are sorted, we maintain the
earliest-starting active interval and extend its end whenever the next
interval overlaps.

The algorithm makes a locally sufficient decision:

``` text
If overlap:
    merge now.
```

There is no need to postpone the merge because a later interval cannot
start before the current next interval's start.

Sorting provides the ordering that makes this greedy decision safe.

------------------------------------------------------------------------

# Why Sorting by Start Is Sufficient

Consider:

``` text
[1, 5]
[2, 3]
[4, 10]
```

After sorting:

``` text
[1, 5]
[2, 3]
[4, 10]
```

The first interval already begins earliest.

As we process:

``` text
[2, 3]
```

it is absorbed into:

``` text
[1, 5]
```

Then:

``` text
[4, 10]
```

also overlaps because:

``` text
4 <= 5
```

so:

``` text
[1, 10]
```

is produced.

Sorting by end time is not the standard ordering for this particular
merge procedure.

------------------------------------------------------------------------

# Relationship to Other Interval Problems

Merge Intervals is a foundational interval pattern.

Once you understand it, related problems become easier to recognize.

Examples include:

``` text
Insert Interval
Interval List Intersections
Meeting Rooms
Meeting Rooms II
Non-overlapping Intervals
Minimum Number of Arrows to Burst Balloons
Employee Free Time
```

However, these problems do not all use exactly the same algorithm.

The important skill is to identify:

``` text
What does the interval problem actually ask?
```

Then select the appropriate interval technique.

------------------------------------------------------------------------

# What the Problem Is Testing

This problem tests several important concepts.

## 1. Sorting

Can you recognize when sorting creates an ordering that simplifies the
problem?

------------------------------------------------------------------------

## 2. Greedy Reasoning

Can you maintain a current merged interval and make the correct local
decision?

------------------------------------------------------------------------

## 3. Invariants

Can you explain what the current interval represents after every
iteration?

------------------------------------------------------------------------

## 4. Boundary Conditions

Can you correctly handle:

``` text
next_start == current_end
```

------------------------------------------------------------------------

## 5. Range Representation

Can you correctly update:

``` text
start
end
```

without losing coverage?

------------------------------------------------------------------------

# Questions to Answer Before Coding

Do not begin by memorizing the code.

Answer these questions first:

1.  What is an interval?
2.  What does it mean for two intervals to overlap?
3.  Why does the input need to be sorted?
4.  Why do we sort by start time?
5.  What is the current interval?
6.  What invariant does the current interval maintain?
7.  How do we detect overlap?
8.  Why is the condition `next_start <= current_end` used?
9.  How do we merge two overlapping intervals?
10. Why do we use `max(current_end, next_end)`?
11. What happens when the intervals do not overlap?
12. When should the current interval be added to the result?
13. Why must the final current interval be added after the loop?
14. What happens with nested intervals?
15. What happens with duplicate intervals?
16. What happens when intervals touch at their boundaries?
17. What happens with an empty input?
18. What is the time complexity?
19. What is the output-space complexity?
20. What is the auxiliary-space complexity?
21. Why is the scan after sorting O(n)?
22. Why is the overall complexity O(n log n)?

------------------------------------------------------------------------

# Expected Problem-Solving Process

Use this sequence during an interview.

## Step 1 --- Clarify the representation

State:

``` text
Each interval is [start, end].
```

------------------------------------------------------------------------

## Step 2 --- Clarify overlap semantics

For sorted intervals:

``` text
next_start <= current_end
```

means overlap under the standard inclusive interpretation.

------------------------------------------------------------------------

## Step 3 --- Consider the input ordering

Ask:

``` text
Are the intervals sorted?
```

If not:

``` text
Sort by start.
```

------------------------------------------------------------------------

## Step 4 --- Define the invariant

State:

> `current` represents the merged interval for the active overlapping
> group.

This demonstrates understanding rather than code memorization.

------------------------------------------------------------------------

## Step 5 --- Process the next interval

If:

``` text
next_start <= current_end
```

merge:

``` text
current_end =
    max(current_end, next_end)
```

Otherwise:

``` text
append current
current = next
```

------------------------------------------------------------------------

## Step 6 --- Finalize

After the loop, append the final current interval.

This final step is easy to forget.

------------------------------------------------------------------------

# Common Mistakes

## Mistake 1 --- Forgetting to sort

Without sorting, the simple greedy scan does not have the ordering it
depends on.

------------------------------------------------------------------------

## Mistake 2 --- Sorting by the wrong field

The standard solution sorts by:

``` text
start
```

not by end.

------------------------------------------------------------------------

## Mistake 3 --- Using `<` instead of `<=`

For standard inclusive intervals:

``` text
[1, 3]
[3, 5]
```

should merge.

Therefore:

``` text
next_start <= current_end
```

is normally used.

------------------------------------------------------------------------

## Mistake 4 --- Incorrectly updating the end

Given:

``` text
current = [1, 10]
next = [2, 5]
```

do not change the end to `5`.

Use:

``` text
max(10, 5)
```

------------------------------------------------------------------------

## Mistake 5 --- Forgetting the final interval

If the final interval is still stored in `current` after the loop, it
must be added to the result.

------------------------------------------------------------------------

## Mistake 6 --- Treating it as a two-pointer problem

Although the scan uses two conceptual intervals, the primary pattern is:

``` text
Sorting + Interval Merging
```

not the standard Two Pointers pattern.

------------------------------------------------------------------------

## Mistake 7 --- Confusing overlapping with containment

Containment is also overlap.

For:

``` text
[1, 10]
[3, 5]
```

the second interval is completely contained in the first.

The merged result is still:

``` text
[1, 10]
```

------------------------------------------------------------------------

# Testing Strategy

A robust implementation should be tested against several categories.

## Basic overlapping intervals

``` text
[
    [1, 3],
    [2, 6]
]
```

Expected:

``` text
[
    [1, 6]
]
```

------------------------------------------------------------------------

## Multiple groups

``` text
[
    [1, 3],
    [2, 6],
    [8, 10],
    [9, 12]
]
```

Expected:

``` text
[
    [1, 6],
    [8, 12]
]
```

------------------------------------------------------------------------

## Unsorted input

``` text
[
    [8, 10],
    [1, 3],
    [9, 12],
    [2, 6]
]
```

Expected:

``` text
[
    [1, 6],
    [8, 12]
]
```

------------------------------------------------------------------------

## Nested intervals

``` text
[
    [1, 10],
    [2, 5]
]
```

Expected:

``` text
[
    [1, 10]
]
```

------------------------------------------------------------------------

## Duplicate intervals

``` text
[
    [1, 5],
    [1, 5]
]
```

Expected:

``` text
[
    [1, 5]
]
```

------------------------------------------------------------------------

## Boundary touching

``` text
[
    [1, 3],
    [3, 5]
]
```

Under standard inclusive interval semantics:

``` text
[
    [1, 5]
]
```

------------------------------------------------------------------------

## No overlap

``` text
[
    [1, 2],
    [4, 5],
    [7, 8]
]
```

Expected:

``` text
[
    [1, 2],
    [4, 5],
    [7, 8]
]
```

------------------------------------------------------------------------

## Empty input

``` text
[]
```

Expected:

``` text
[]
```

------------------------------------------------------------------------

## Single interval

``` text
[
    [10, 20]
]
```

Expected:

``` text
[
    [10, 20]
]
```

------------------------------------------------------------------------

# Interview Follow-Up Questions

After solving the basic problem, be ready for:

1.  Why do we sort by start time?
2.  Can the problem be solved without sorting?
3.  What is the complexity of your solution?
4.  What invariant are you maintaining?
5.  Why do you use `max` when merging?
6.  What happens when intervals only touch?
7.  What if intervals are half-open instead of inclusive?
8.  How would you modify the algorithm for half-open intervals?
9.  How would you solve Insert Interval?
10. How would you find the maximum number of overlapping intervals?
11. How would you solve Meeting Rooms II?
12. How would you find whether any two intervals overlap?
13. How would you merge intervals arriving as a stream?
14. What if the intervals are already sorted?
15. Can you reduce the work if the input is already sorted?
16. How would you handle very large numbers of intervals?
17. What if intervals arrive continuously from multiple sources?
18. How would you distribute interval merging?
19. What changes if the intervals have associated metadata?
20. What if you need to preserve the original interval identifiers?

------------------------------------------------------------------------

# Variations You Should Recognize

## Variation 1 --- Insert Interval

You are given already sorted, non-overlapping intervals and one new
interval.

The problem becomes:

``` text
Before overlap
     ↓
Overlap region
     ↓
After overlap
```

This is related to Merge Intervals but can be solved without sorting the
entire collection when the existing intervals are already sorted.

------------------------------------------------------------------------

## Variation 2 --- Interval Intersection

Given two lists of intervals, find their common ranges.

This uses a different scanning strategy.

The key question becomes:

``` text
What range do both intervals cover?
```

------------------------------------------------------------------------

## Variation 3 --- Meeting Rooms

Determine whether a person can attend all meetings.

This becomes an overlap-detection problem.

After sorting by start:

``` text
if next_start < previous_end:
    conflict
```

The exact boundary condition depends on the meeting interval semantics.

------------------------------------------------------------------------

## Variation 4 --- Meeting Rooms II

Find the minimum number of rooms required.

This often leads to:

``` text
sort
+
min heap
```

or:

``` text
event/sweep-line
```

The important point is that not every interval problem is solved by
simply merging.

------------------------------------------------------------------------

# Pattern Recognition Summary

When you see:

``` text
Intervals
Ranges
Start / End
Overlapping segments
Schedules
Time ranges
```

think:

``` text
INTERVAL PATTERN
```

Then ask:

``` text
Are intervals sorted?
        ↓
       NO
        ↓
Sort by start
        ↓
Scan
        ↓
Overlap?
   ↙         ↘
 YES          NO
 ↓             ↓
Merge       Finalize
```

For Merge Intervals specifically:

``` text
Sort by start
      ↓
Maintain current
      ↓
next_start <= current_end?
      ↓
   YES          NO
    ↓            ↓
Extend       Append current
    ↓            ↓
continue     Start new current
```

------------------------------------------------------------------------

# Definition of Done

Before considering this problem complete, you should be able to:

-   [ ] State the problem clearly without looking at notes.
-   [ ] Define an interval.
-   [ ] Define interval overlap.
-   [ ] Explain the boundary-touching case.
-   [ ] Identify the Interval pattern.
-   [ ] Explain why sorting is useful.
-   [ ] Explain why intervals are sorted by start.
-   [ ] Define the current-interval invariant.
-   [ ] Detect overlap correctly.
-   [ ] Merge intervals correctly.
-   [ ] Explain why `max(current_end, next_end)` is required.
-   [ ] Handle nested intervals.
-   [ ] Handle duplicate intervals.
-   [ ] Handle unsorted input.
-   [ ] Handle empty input.
-   [ ] Handle a single interval.
-   [ ] Explain the sorting complexity.
-   [ ] Explain the scan complexity.
-   [ ] Distinguish output space from auxiliary space.
-   [ ] Implement the algorithm independently.
-   [ ] Answer interval-pattern follow-up questions.
-   [ ] Explain how Merge Intervals differs from related interval
    problems.

------------------------------------------------------------------------

# Interview Prompt

> **Given an array of intervals where `intervals[i] = [start_i, end_i]`,
> merge all overlapping intervals and return an array of the
> non-overlapping intervals that cover all the intervals in the input.**

Example:

``` text
Input:
[
    [1, 3],
    [2, 6],
    [8, 10],
    [9, 12]
]

Output:
[
    [1, 6],
    [8, 12]
]
```

Your first task in an interview is **not to code immediately**.

Start by explaining:

1.  What an interval represents.
2.  What it means for two intervals to overlap.
3.  Why the input order matters.
4.  Why sorting by start simplifies the problem.
5.  What the current interval represents.
6.  How overlap is detected.
7.  How two overlapping intervals are merged.
8.  Why `max(current_end, next_end)` is necessary.
9.  What happens when intervals do not overlap.
10. Why the final interval must be added after the loop.
11. The time complexity.
12. The space complexity.
13. Important edge cases.

Then implement the solution independently.

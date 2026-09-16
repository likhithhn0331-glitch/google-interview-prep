# Longest Consecutive Sequence

## Problem Statement

Given an unsorted array of integers `nums`, find the length of the
longest consecutive elements sequence.

A **consecutive sequence** is a sequence of integers in which each
number is exactly one greater than the previous number.

For example:

``` text
[1, 2, 3, 4]
```

is a consecutive sequence because:

``` text
2 = 1 + 1
3 = 2 + 1
4 = 3 + 1
```

The task is **not** to return the actual sequence. The task is to return
the **length** of the longest consecutive sequence that can be formed
from the numbers in the input.

The input array is unsorted, so the numbers may appear in any order.

------------------------------------------------------------------------

## Formal Input

You are given:

``` text
nums: an array/list of integers
```

Example:

``` text
nums = [100, 4, 200, 1, 3, 2]
```

The elements are not necessarily sorted.

------------------------------------------------------------------------

## Expected Output

Return a single integer representing the length of the longest sequence
of consecutive integers that can be formed from the input.

For:

``` text
nums = [100, 4, 200, 1, 3, 2]
```

the longest consecutive sequence is:

``` text
1, 2, 3, 4
```

Therefore the answer is:

``` text
4
```

------------------------------------------------------------------------

## Important Clarification

The consecutive numbers **do not need to appear next to one another in
the original array**.

For example:

``` text
nums = [100, 4, 200, 1, 3, 2]
```

The values:

``` text
1, 2, 3, 4
```

are separated throughout the input.

Nevertheless, they form a consecutive sequence.

Therefore, the problem is about the **values present in the array**, not
about contiguous positions in the original array.

This distinction is extremely important.

------------------------------------------------------------------------

## Example 1

### Input

``` text
nums = [100, 4, 200, 1, 3, 2]
```

The consecutive sequences include:

``` text
1, 2, 3, 4
```

and individual values such as:

``` text
100
200
```

The longest sequence has length:

``` text
4
```

### Output

``` text
4
```

------------------------------------------------------------------------

## Example 2

### Input

``` text
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
```

The values:

``` text
0, 1, 2, 3, 4, 5, 6, 7, 8
```

form a consecutive sequence.

Its length is:

``` text
9
```

### Output

``` text
9
```

The duplicate `0` does not create an additional element in the
consecutive sequence.

------------------------------------------------------------------------

## Example 3

### Input

``` text
nums = []
```

There are no numbers, so there is no consecutive sequence.

### Output

``` text
0
```

------------------------------------------------------------------------

## Example 4

### Input

``` text
nums = [1]
```

A single number is itself a consecutive sequence of length `1`.

### Output

``` text
1
```

------------------------------------------------------------------------

## Example 5

### Input

``` text
nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -2, 6, 0, 2]
```

The values:

``` text
-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

form a consecutive sequence.

The sequence length is:

``` text
12
```

The duplicate `0` does not change the sequence length.

------------------------------------------------------------------------

# Pattern Classification

This problem belongs to the:

``` text
Hashing
```

pattern.

More specifically:

``` text
Hash Set + Sequence Start Detection
```

The key pattern-recognition clue is:

> **When you need fast membership checks for values and the input does
> not need to preserve ordering, consider a Hash Set.**

The central structure is:

``` text
Input array
    ↓
Hash Set
    ↓
Fast membership lookup
    ↓
Find sequence starts
    ↓
Expand consecutive sequence
    ↓
Track maximum length
```

------------------------------------------------------------------------

# Core Challenge

At first glance, the problem looks like a sorting problem.

A natural approach is:

``` text
sort the numbers
    ↓
scan from left to right
    ↓
find the longest consecutive run
```

That approach works.

However, the important challenge is to recognize that the problem can be
solved in **expected O(n)** time using a Hash Set.

The key question is:

> How can we determine whether a number is the beginning of a
> consecutive sequence without sorting the entire array?

The answer is to check whether:

``` text
number - 1
```

exists.

If:

``` text
x - 1
```

does not exist, then `x` is the beginning of a consecutive sequence.

For example, suppose:

``` text
x = 4
```

and the set contains:

``` text
1, 2, 3, 4, 5, 6
```

Since:

``` text
3
```

exists, `4` is **not** the beginning of the sequence.

But if:

``` text
x = 1
```

and:

``` text
0
```

does not exist, then `1` is the beginning of the sequence.

This observation is the heart of the optimal approach.

------------------------------------------------------------------------

# Sequence Start Detection

Consider:

``` text
nums = [100, 4, 200, 1, 3, 2]
```

Convert the values into a set:

``` text
{
    100,
    4,
    200,
    1,
    3,
    2
}
```

Now consider `1`.

Check:

``` text
1 - 1 = 0
```

`0` is not in the set.

Therefore:

``` text
1
```

is a sequence start.

We can then expand:

``` text
1
1 + 1 = 2
2 + 1 = 3
3 + 1 = 4
4 + 1 = 5
```

`5` is not present.

Therefore the sequence length is:

``` text
4
```

------------------------------------------------------------------------

# Why Sequence Start Detection Matters

A naive Hash Set solution might attempt to expand a sequence starting
from **every** number.

That can cause repeated work.

For:

``` text
1, 2, 3, 4, 5
```

starting from every value would produce:

``` text
1 → 2 → 3 → 4 → 5
2 → 3 → 4 → 5
3 → 4 → 5
4 → 5
5
```

The same sequence is repeatedly traversed.

Instead, only begin expanding when:

``` text
x - 1
```

is absent.

For:

``` text
1, 2, 3, 4, 5
```

only:

``` text
1
```

is a sequence start.

Therefore:

``` text
1 → 2 → 3 → 4 → 5
```

is traversed once.

This is the key optimization.

------------------------------------------------------------------------

# Important Observation

For any number `x`:

``` text
if x - 1 exists:
    x is not the start of a sequence
```

and:

``` text
if x - 1 does not exist:
    x is the start of a sequence
```

Once a sequence start is identified, repeatedly check:

``` text
x + 1
x + 2
x + 3
...
```

until the next value is absent.

------------------------------------------------------------------------

# Hash Set Mental Model

Think of the Hash Set as answering:

``` text
"Does this number exist?"
```

For example:

``` text
set = {1, 2, 3, 4, 100, 200}
```

Membership checks are expected O(1):

``` text
1 in set?     → yes
0 in set?     → no
3 in set?     → yes
5 in set?     → no
100 in set?   → yes
```

This allows the algorithm to explore consecutive values without sorting.

------------------------------------------------------------------------

# Why a Hash Set Instead of a Hash Map?

The problem primarily requires:

``` text
Does this value exist?
```

It does not initially require:

``` text
value → additional information
```

Therefore a:

``` text
Hash Set
```

is sufficient.

Compare:

``` text
Hash Set:
value → exists
```

with:

``` text
Hash Map:
key → value
```

For this problem, membership is the central operation.

------------------------------------------------------------------------

# Duplicate Values

Duplicates are an important edge case.

Consider:

``` text
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
```

There are two `0`s.

However, the sequence is:

``` text
0, 1, 2, 3, 4, 5, 6, 7, 8
```

The duplicate `0` should not make the sequence length `10`.

Therefore:

``` text
set(nums)
```

naturally removes duplicates.

The resulting set contains:

``` text
{0, 1, 2, 3, 4, 5, 6, 7, 8}
```

and the longest sequence length is:

``` text
9
```

------------------------------------------------------------------------

# What the Problem Is Testing

This problem tests several important concepts.

## 1. Hash Set

You need to understand when fast membership testing is more useful than
ordering.

------------------------------------------------------------------------

## 2. Pattern Recognition

When you see:

> "Find the longest sequence of consecutive values in an unsorted
> collection."

You should consider:

``` text
Hash Set
+
Sequence Start Detection
```

------------------------------------------------------------------------

## 3. Avoiding Unnecessary Sorting

Sorting is an obvious solution:

``` text
O(n log n)
```

But the Hash Set approach can achieve expected:

``` text
O(n)
```

by trading additional memory for faster membership checks.

------------------------------------------------------------------------

## 4. Avoiding Repeated Work

The most important optimization is not simply:

``` text
Use a Hash Set
```

It is:

``` text
Only expand from sequence starts.
```

That is what prevents repeated traversal of the same sequence.

------------------------------------------------------------------------

# Brute-Force Approach

A conceptual brute-force solution could repeatedly search for the next
value.

For example:

``` text
For every number x:
    check whether x + 1 exists
    check whether x + 2 exists
    check whether x + 3 exists
    ...
```

If membership checking is performed by scanning the original array, each
lookup can cost O(n).

This can lead to very poor performance.

The approach also repeats work for many starting values.

------------------------------------------------------------------------

# Sorting-Based Approach

A common solution is:

``` text
1. Sort nums.
2. Scan the sorted array.
3. Count consecutive values.
4. Track the maximum.
```

For:

``` text
[100, 4, 200, 1, 3, 2]
```

sorting gives:

``` text
[1, 2, 3, 4, 100, 200]
```

Now the consecutive sequence is immediately visible:

``` text
1 → 2 → 3 → 4
```

### Complexity

Sorting generally costs:

``` text
O(n log n)
```

followed by:

``` text
O(n)
```

for the scan.

Overall:

``` text
O(n log n)
```

------------------------------------------------------------------------

# Hash Set Approach

The Hash Set approach is:

``` text
1. Put every number into a set.
2. Iterate through the numbers.
3. Check whether x - 1 exists.
4. If x - 1 does not exist, x is a sequence start.
5. Expand using x + 1, x + 2, ...
6. Track the longest sequence.
```

The central condition is:

``` text
if x - 1 not in num_set:
```

Then:

``` text
current = x
length = 1

while current + 1 in num_set:
    current += 1
    length += 1
```

Finally:

``` text
answer = max(answer, length)
```

The above is the algorithmic idea; implement it yourself rather than
copying a memorized template.

------------------------------------------------------------------------

# Complexity

Let:

``` text
n = number of input elements
```

Creating the set requires expected:

``` text
O(n)
```

membership checks are expected:

``` text
O(1)
```

The important reasoning is that sequence expansion happens only from
sequence starts.

Therefore the overall expected time complexity is:

``` text
O(n)
```

with:

``` text
O(n)
```

additional space for the set.

------------------------------------------------------------------------

# Why the Expansion Is Still O(n)

At first glance, the nested-looking structure:

``` text
for each number:
    while next number exists:
        advance
```

may appear to be:

``` text
O(n²)
```

But sequence expansion only begins at numbers that do not have a
predecessor.

For a sequence:

``` text
1, 2, 3, 4, 5
```

only `1` starts expansion.

The values:

``` text
2
3
4
5
```

are not sequence starts because their predecessors exist.

Therefore the long sequence is traversed once rather than once from
every element.

This is a critical complexity-analysis point.

------------------------------------------------------------------------

# Edge Cases

## 1. Empty array

``` text
[]
```

Expected:

``` text
0
```

------------------------------------------------------------------------

## 2. One element

``` text
[10]
```

Expected:

``` text
1
```

------------------------------------------------------------------------

## 3. No consecutive values

``` text
[10, 30, 50, 70]
```

Every value forms a sequence of length `1`.

Expected:

``` text
1
```

------------------------------------------------------------------------

## 4. All values consecutive

``` text
[1, 2, 3, 4, 5]
```

Expected:

``` text
5
```

------------------------------------------------------------------------

## 5. Unordered values

``` text
[5, 2, 4, 1, 3]
```

Expected:

``` text
5
```

The original ordering does not matter.

------------------------------------------------------------------------

## 6. Duplicate values

``` text
[1, 2, 2, 3]
```

The sequence is:

``` text
1, 2, 3
```

Expected:

``` text
3
```

------------------------------------------------------------------------

## 7. Negative values

``` text
[-3, -2, -1, 0, 1]
```

Expected:

``` text
5
```

The algorithm must work with negative integers.

------------------------------------------------------------------------

## 8. Multiple sequences

``` text
[1, 2, 3, 10, 11, 12, 13]
```

Sequences:

``` text
1, 2, 3
```

and:

``` text
10, 11, 12, 13
```

The longest sequence has length:

``` text
4
```

------------------------------------------------------------------------

# Questions to Answer Before Coding

Do not begin by memorizing the implementation.

Answer these questions first:

1.  What exactly is a consecutive sequence?
2.  Does the original array need to be sorted?
3.  Do consecutive values need to be adjacent in the original array?
4.  Why is a Hash Set useful?
5.  What operation do we need the Hash Set to perform?
6.  How can we identify the beginning of a sequence?
7.  Why do we check `x - 1`?
8.  Why should we only expand from sequence starts?
9.  How do duplicates affect the problem?
10. Why can sorting solve the problem?
11. What is the complexity of the sorting approach?
12. What is the expected complexity of the Hash Set approach?
13. Why doesn't the `for` loop plus `while` loop automatically imply
    O(n²)?
14. What is the space complexity?
15. What happens for negative numbers?
16. What happens for an empty input?
17. Why is a Hash Set sufficient instead of a Hash Map?

------------------------------------------------------------------------

# Expected Problem-Solving Process

Use this sequence during an interview.

## Step 1 --- Understand the requirement

Identify:

``` text
Input:
unsorted array of integers

Output:
length of longest consecutive value sequence
```

------------------------------------------------------------------------

## Step 2 --- Clarify adjacency

Important distinction:

``` text
Array adjacency
```

is not required.

The values only need to form a consecutive numerical sequence.

For example:

``` text
[4, 1, 3, 2]
```

contains:

``` text
1, 2, 3, 4
```

even though the values are not ordered in the input.

------------------------------------------------------------------------

## Step 3 --- Consider the obvious solution

Think:

``` text
Sort
↓
Scan
↓
Count consecutive values
```

This gives:

``` text
O(n log n)
```

------------------------------------------------------------------------

## Step 4 --- Ask whether sorting is necessary

The real operation we need is:

``` text
Does x exist?
```

That suggests:

``` text
Hash Set
```

------------------------------------------------------------------------

## Step 5 --- Identify sequence starts

For every `x`:

``` text
if x - 1 is absent:
    x is a sequence start
```

This prevents repeated traversal.

------------------------------------------------------------------------

## Step 6 --- Expand the sequence

Starting at `x`:

``` text
x
x + 1
x + 2
x + 3
...
```

Continue while each next value exists in the set.

------------------------------------------------------------------------

## Step 7 --- Track the maximum

Maintain:

``` text
longest
```

and update it whenever a longer sequence is found.

------------------------------------------------------------------------

# Pattern Recognition Summary

When you see:

``` text
"Find the longest consecutive sequence in an unsorted array."
```

think:

``` text
Unsorted values
      ↓
Need fast membership
      ↓
Hash Set
      ↓
Find sequence starts
      ↓
Expand consecutive values
      ↓
Track maximum
```

The reusable pattern is:

``` text
Hash Set
+
Membership Check
+
Start Detection
+
Linear Expansion
```

------------------------------------------------------------------------

# Common Mistakes

## Mistake 1 --- Sorting immediately

Sorting works, but if the goal is expected O(n), you should recognize
the Hash Set solution.

------------------------------------------------------------------------

## Mistake 2 --- Expanding from every number

This causes unnecessary repeated work.

Only expand when:

``` text
x - 1
```

does not exist.

------------------------------------------------------------------------

## Mistake 3 --- Treating the problem as a contiguous subarray problem

The sequence does not need to be contiguous in the original array.

For:

``` text
[100, 4, 200, 1, 3, 2]
```

the sequence:

``` text
1, 2, 3, 4
```

is valid.

------------------------------------------------------------------------

## Mistake 4 --- Forgetting duplicates

Duplicates should not increase the length of the consecutive sequence.

A Hash Set naturally handles this.

------------------------------------------------------------------------

## Mistake 5 --- Assuming nested loops automatically mean O(n²)

The inner expansion is only performed from sequence starts.

A proper complexity analysis must account for that property.

------------------------------------------------------------------------

## Mistake 6 --- Using a Hash Map unnecessarily

If the only requirement is:

``` text
Does x exist?
```

a Hash Set is sufficient.

------------------------------------------------------------------------

## Mistake 7 --- Forgetting negative numbers

The definition of consecutive integers works equally well for:

``` text
-3, -2, -1, 0, 1
```

------------------------------------------------------------------------

# Interview Follow-Up Questions

After solving the basic problem, be ready for:

1.  Can you solve it in O(n) expected time?
2.  Why is sorting unnecessary?
3.  Why do you check `x - 1`?
4.  Why does sequence-start detection prevent repeated work?
5.  What happens with duplicate values?
6.  What is the worst-case behavior of a hash table?
7.  What assumptions are made when we say Hash Set operations are
    expected O(1)?
8.  What is the space complexity?
9.  Can you solve it with sorting?
10. Compare the sorting and Hash Set approaches.
11. What if memory is severely constrained?
12. What if the input arrives as a stream?
13. How would you handle a dataset too large to fit in memory?
14. How would you distribute this computation?
15. Can you find the actual longest sequence rather than only its
    length?
16. What changes if you need the sequence itself?
17. How would you test this implementation?
18. What happens if the input contains very large positive or negative
    integers?

------------------------------------------------------------------------

# Testing Strategy

A good implementation should be tested against multiple categories.

## Basic

``` text
[100, 4, 200, 1, 3, 2]
→ 4
```

------------------------------------------------------------------------

## Fully consecutive

``` text
[1, 2, 3, 4, 5]
→ 5
```

------------------------------------------------------------------------

## No consecutive values

``` text
[10, 20, 30]
→ 1
```

------------------------------------------------------------------------

## Duplicate values

``` text
[1, 2, 2, 3]
→ 3
```

------------------------------------------------------------------------

## Negative numbers

``` text
[-3, -2, -1, 0, 1]
→ 5
```

------------------------------------------------------------------------

## Multiple sequences

``` text
[1, 2, 3, 10, 11, 12, 13]
→ 4
```

------------------------------------------------------------------------

## Empty input

``` text
[]
→ 0
```

------------------------------------------------------------------------

## Single element

``` text
[7]
→ 1
```

------------------------------------------------------------------------

# Definition of Done

Before considering this problem complete, you should be able to:

-   [ ] State the problem clearly without looking at notes.
-   [ ] Explain what a consecutive sequence means.
-   [ ] Explain why array ordering does not matter.
-   [ ] Identify the Hash Set pattern.
-   [ ] Explain why membership checks are required.
-   [ ] Explain sequence-start detection.
-   [ ] Explain why `x - 1` is checked.
-   [ ] Explain why expansion should happen only from sequence starts.
-   [ ] Explain how duplicates are handled.
-   [ ] Solve the problem using a Hash Set independently.
-   [ ] Explain the sorting-based alternative.
-   [ ] Compare O(n log n) sorting with expected O(n) hashing.
-   [ ] Explain why the Hash Set solution is expected O(n).
-   [ ] Explain why the nested-looking loops do not necessarily produce
    O(n²).
-   [ ] State the space complexity.
-   [ ] Handle empty input.
-   [ ] Handle negative values.
-   [ ] Handle duplicate values.
-   [ ] Answer interview follow-up questions.
-   [ ] Implement the solution without copying a memorized template.

------------------------------------------------------------------------

# Interview Prompt

> **Given an unsorted array of integers `nums`, return the length of the
> longest consecutive elements sequence.**

Example:

``` text
Input:
[100, 4, 200, 1, 3, 2]

Output:
4
```

Explanation:

``` text
The longest consecutive sequence is:

1, 2, 3, 4

Therefore the length is:

4
```

Your first task in an interview is **not to code immediately**.

Start by explaining:

1.  What constitutes a consecutive sequence.
2.  Why the original array does not need to be sorted.
3.  The obvious sorting-based solution.
4.  Why a Hash Set can avoid sorting.
5.  How sequence-start detection works.
6.  Why checking `x - 1` is important.
7.  Why the expected time complexity is O(n).
8.  The space complexity.
9.  Important edge cases.

Then implement the solution independently.

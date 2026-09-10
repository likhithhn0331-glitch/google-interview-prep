# Two Sum — DSA Problem Statement

## Problem

Given an array of integers `nums` and an integer `target`, find **two distinct indices** `i` and `j` such that:

```text
nums[i] + nums[j] = target
```

Return the **indices** of these two numbers.

## Constraints

- Each input has **exactly one solution**.
- You cannot use the **same element twice**.
- The order of the returned indices does not matter.

## Example 1

**Input:**

```text
nums = [2, 7, 11, 15]
target = 9
```

**Output:**

```text
[0, 1]
```

**Explanation:**

```text
nums[0] + nums[1]
= 2 + 7
= 9
```

## Example 2

**Input:**

```text
nums = [3, 2, 4]
target = 6
```

**Output:**

```text
[1, 2]
```

**Explanation:**

```text
nums[1] + nums[2]
= 2 + 4
= 6
```

## Example 3

**Input:**

```text
nums = [3, 3]
target = 6
```

**Output:**

```text
[0, 1]
```

## What You Should Think About

Before coding, ask:

> **For every number `x`, what number do I need to find to reach the target?**

The answer is:

```text
complement = target - x
```

This problem is excellent for learning the **Hash Map / Dictionary** pattern.

## Goal

First try to solve it yourself.

Don't worry about the optimal solution yet.

### Practice

Try solving the problem using:

1. **Brute Force**
2. **Hash Map / Dictionary**

For each approach, identify:

- Time complexity
- Space complexity
- Why the approach works

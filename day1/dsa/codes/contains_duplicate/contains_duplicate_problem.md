# Contains Duplicate — DSA Problem Statement

## Problem

Given an integer array `nums`, return `true` if **any value appears at least twice** in the array, and return `false` if **every element is distinct**.

## Examples

### Example 1

**Input:**

```text
nums = [1, 2, 3, 1]
```

**Output:**

```text
true
```

**Explanation:**

The value `1` appears twice.

---

### Example 2

**Input:**

```text
nums = [1, 2, 3, 4]
```

**Output:**

```text
false
```

**Explanation:**

Every element appears exactly once.

---

### Example 3

**Input:**

```text
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
```

**Output:**

```text
true
```

**Explanation:**

Several values appear more than once.

## Constraints

- `1 <= nums.length <= 10⁵`
- `-10⁹ <= nums[i] <= 10⁹`

## What You Should Think About

Ask yourself:

> **How can I efficiently keep track of the numbers I've already seen?**

A useful data structure to consider is a:

```text
Set
```

## Goal

Try solving it using:

1. **Brute Force**
2. **Sorting**
3. **Hash Set**

For each approach, identify:

- Time complexity
- Space complexity
- Why the approach works

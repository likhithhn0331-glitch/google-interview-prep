# Valid Anagram — DSA Problem Statement

## Problem

Given two strings `s` and `t`, return `true` if `t` is an **anagram** of `s`, and `false` otherwise.

An **anagram** is a word or phrase formed by rearranging the letters of another word or phrase, using **all the original letters exactly once**.

## Examples

### Example 1

**Input:**

```text
s = "anagram"
t = "nagaram"
```

**Output:**

```text
true
```

**Explanation:**

Both strings contain exactly the same characters with the same frequencies:

```text
a → 3
n → 1
g → 1
r → 1
m → 1
```

---

### Example 2

**Input:**

```text
s = "rat"
t = "car"
```

**Output:**

```text
false
```

**Explanation:**

The strings do not contain the same characters.

```text
s → r, a, t
t → c, a, r
```

` t ` contains `c` instead of `t`.

---

### Example 3

**Input:**

```text
s = "listen"
t = "silent"
```

**Output:**

```text
true
```

**Explanation:**

Both strings contain the same characters with the same frequencies.

## Constraints

- `1 <= s.length, t.length <= 5 × 10⁴`
- `s` and `t` consist of lowercase English letters.

## What You Should Think About

Ask yourself:

> **If two strings are anagrams, what must be true about the frequency of every character?**

For example:

```text
s = "aabbc"
t = "cbaba"
```

Character frequencies:

```text
a → 2
b → 2
c → 1
```

Since the frequencies are identical, the strings are anagrams.

## Possible Approaches

Try solving the problem using:

1. **Sorting**
2. **Hash Map / Dictionary**
3. **Character Frequency Array**

For each approach, identify:

- Time complexity
- Space complexity
- Why the approach works

## Key DSA Pattern

**Hash Map / Frequency Counting**

The important idea is to count how many times each character appears and compare the frequencies between the two strings.

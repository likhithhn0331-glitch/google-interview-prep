# Valid Palindrome — DSA Problem Statement

## Problem

Given a string `s`, determine whether it is a **palindrome**, considering only **alphanumeric characters** and ignoring **case**.

A palindrome is a string that reads the same forward and backward after removing all non-alphanumeric characters and ignoring case differences.

## Examples

### Example 1

```text
Input:  s = "A man, a plan, a canal: Panama"
Output: true
```

**Explanation:**

After removing non-alphanumeric characters and converting to lowercase:

```text
"amanaplanacanalpanama"
```

This reads the same forward and backward.

---

### Example 2

```text
Input:  s = "race a car"
Output: false
```

**Explanation:**

After cleaning:

```text
"raceacar"
```

This is not a palindrome.

---

### Example 3

```text
Input:  s = " "
Output: true
```

**Explanation:**

After removing non-alphanumeric characters, the string is empty. An empty string is considered a palindrome.

## Constraints

- `1 <= s.length <= 2 × 10^5`
- `s` consists of printable ASCII characters.

## Expected Approach

Try solving this using the **Two Pointers** technique.

Use:

```text
left  → beginning of string
right → end of string
```

Move the pointers toward each other while:

1. Skipping non-alphanumeric characters.
2. Comparing characters after converting them to lowercase.
3. Returning `false` if the characters don't match.
4. Returning `true` if the pointers meet/cross without finding a mismatch.

## Target Complexity

```text
Time:  O(n)
Space: O(1)
```

## Interview Follow-up

Can you solve it **without creating a cleaned/normalized copy of the string**?

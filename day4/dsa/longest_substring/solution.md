# Solution for Longest Substring Without Repeating Characters

## Problem recap

Given a string `s`, find the length of the longest substring that contains no repeated characters.

Example:

- Input: `s = "abcabcbb"`
- Output: `3`
- Explanation: `"abc"` is the longest substring without repeating characters.

## 1) Brute force approach

The simplest idea is to check every substring and see whether it contains duplicates.

### How it works

- Choose each starting index `i`.
- Extend the substring from `i` to the right.
- Keep a set of seen characters.
- If a repeated character appears, stop expanding that substring.
- Track the longest valid substring length seen so far.

### Code

```python
def longest_substring_brute_force(s):
    n = len(s)
    max_length = 0
    for i in range(n):
        seen = set()
        current_length = 0
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            current_length += 1
        max_length = max(max_length, current_length)
    return max_length
```

### Why this works

Each substring starting at `i` is examined fully until a duplicate is found. The algorithm keeps the maximum valid length across all substrings.

### Time complexity

- Outer loop: `O(n)`
- Inner loop: worst case `O(n)`
- Total: `O(n^2)`

### Space complexity

- We store a set for the current substring.
- Worst-case space: `O(k)` where `k` is the length of the current substring, up to `O(n)`.

### Disadvantages

This approach is easy to understand, but it is inefficient for long strings because it checks many overlapping substrings repeatedly.

---

## 2) Sliding window approach

Instead of re-checking all substrings from scratch, we maintain a dynamic window of valid characters and move its boundaries as needed.

### Key idea

A valid substring is a window where all characters are unique.

- Keep a left pointer and a right pointer.
- Expand the window by moving the right pointer.
- If the character at `right` is already in the current window, move `left` forward until the duplicate is removed.
- Track the maximum size of the window.

This is called the sliding window technique.

### Code

```python
def longest_substring_sliding_window(s):
    n = len(s)
    char_index_map = {}
    max_length = 0
    left = 0

    for right in range(n):
        if s[right] in char_index_map and char_index_map[s[right]] >= left:
            left = char_index_map[s[right]] + 1
        char_index_map[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length
```

### Why this works

- `char_index_map` stores the most recent index of each character.
- If the current character repeats inside the valid window, then the previous occurrence is before `left` and must be discarded.
- We move `left` to just after that previous index.
- The window remains valid at every step.
- The maximum valid window size is updated continuously.

### Example walkthrough

For `s = "abcabcbb"`:

- `a b c` → valid window length 3
- next `a` repeats → move `left` to remove previous `a`
- window becomes valid again
- continue until all characters are processed
- maximum valid window length found is `3`

---

## 3) Comparison: brute force vs sliding window

### Brute force

- Checks all substrings.
- Repeats work unnecessarily.
- Time complexity: `O(n^2)`.
- Easy to write and reason about.

### Sliding window

- Reuses information from previous windows.
- Avoids re-scanning characters that are already known to be outside the current valid window.
- Time complexity: `O(n)`.
- Space complexity: `O(n)` in the worst case.
- Better for interview problems and production-scale input.

### Why sliding window is better

The brute force method does repeated checking of overlapping substrings. For example, if a window is already known to contain valid characters, we do not need to rebuild it from scratch every time. The sliding window keeps only the necessary state, which reduces the total work significantly.

---

## 4) Complexity summary

| Approach | Time | Space | Notes |
| --- | --- | --- | --- |
| Brute force | `O(n^2)` | `O(n)` | Simple but slow |
| Sliding window | `O(n)` | `O(n)` | Efficient and standard for this problem |

Where `n` is the length of the string.

---

## 5) When to use this pattern

Use sliding window when:

- You are dealing with a string or array
- You need the longest/shortest valid contiguous segment
- The window condition can be checked incrementally
- You want to avoid `O(n^2)` repeated scanning

This problem is a classic example of a sliding window problem because it asks for the longest contiguous segment that satisfies a uniqueness constraint.

---

## 6) Key takeaway

The brute force solution is useful for learning the idea, but the sliding window is the optimal approach for this problem.

The sliding window solution is preferred because it reduces time complexity from quadratic to linear while keeping the logic clean and efficient.

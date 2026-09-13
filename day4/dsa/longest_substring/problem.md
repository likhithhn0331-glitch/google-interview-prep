# Longest Substring Without Repeating Characters

## Problem Statement

Given a string `s`, find the length of the longest substring that does not contain any repeated characters.

A substring is a contiguous sequence of characters within the string.

Example:

- Input: `s = "abcabcbb"`
- Output: `3`
- Explanation: `"abc"` is the longest substring without repeating characters.

Another example:

- Input: `s = "bbbbb"`
- Output: `1`
- Explanation: The longest substring without repeating characters is `"b"`.

Another example:

- Input: `s = "pwwkew"`
- Output: `3`
- Explanation: `"wke"` is the longest substring without repeating characters.

## Key Idea

We need to keep track of the longest window where all characters are unique.

A good way to do this is by using the sliding window technique:

- Maintain a window `[left, right]` that contains only unique characters.
- Expand the right pointer to include new characters.
- If a character repeats inside the current window, move the left pointer forward until the duplicate is removed.
- Track the maximum window length seen so far.

## Efficient Approach

Use a hash map (or set) to store the last index of each character seen in the current window.

### Algorithm

1. Initialize two pointers: `left = 0` and `maxLength = 0`.
2. Use a hash map `lastSeen` to store the most recent index of each character.
3. Traverse the string with `right` from `0` to `n - 1`:
   - If `s[right]` is already in the current window, update `left` to `max(left, lastSeen[s[right]] + 1)`.
   - Update `lastSeen[s[right]] = right`.
   - Compute `maxLength = max(maxLength, right - left + 1)`.
4. Return `maxLength`.

## Why This Works

At every step:

- The window from `left` to `right` contains no repeated characters.
- When a duplicate appears, sliding `left` forward removes the earlier occurrence from the window.
- This guarantees that the current window always stays valid.
- The longest valid window found during the scan is the answer.

## Time Complexity

- Each character is processed at most twice (once when entering the window and once when moving `left` past it).
- Time complexity: `O(n)`
- Space complexity: `O(min(n, character_set_size))` in the worst case, which is `O(n)` for a string with all distinct characters.

## Example Walkthrough

For `s = "abcabcbb"`:

- Start with empty window
- Add `a`, `b`, `c` → window is `"abc"`, length 3
- Add `a` again → duplicate found, move left to after the previous `a`
- Window becomes `"bca"` → still valid, length 3
- Continue through the string
- Best valid window found is `"abc"` or `"bca"`, length 3

## Edge Cases

- Empty string: output should be `0`
- All characters same: output should be `1`
- All characters distinct: output should be length of the string
- Small strings and repeated pattern strings should also work correctly

## Python Example

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        last_seen = {}
        max_length = 0

        for right, ch in enumerate(s):
            if ch in last_seen:
                left = max(left, last_seen[ch] + 1)

            last_seen[ch] = right
            max_length = max(max_length, right - left + 1)

        return max_length
```

## Interview Tip

This is a classic sliding window problem. If you see a requirement like "longest contiguous segment with unique characters," think about maintaining a valid window and moving pointers efficiently instead of checking all substrings.

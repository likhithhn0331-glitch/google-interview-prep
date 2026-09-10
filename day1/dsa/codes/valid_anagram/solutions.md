# Valid Anagram Solutions

A valid anagram means both strings contain the same characters in the same frequency, just in a different order.

## 1) Brute Force Approach

### Idea
- Check if both strings have the same length.
- For each character in the first string, try to find a matching unused character in the second string.
- If a match is not found, return `False`.

### Python Example
```python
def valid_anagram_brute_force(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    used_indices = []

    for char in str_1:
        found = False
        for i in range(len(str_2)):
            if str_2[i] == char and i not in used_indices:
                used_indices.append(i)
                found = True
                break
        if not found:
            return False

    return True
```

### Time Complexity
- Outer loop: O(n)
- Inner loop: O(n)
- Total: O(n^2)

### Space Complexity
- `used_indices` can store up to `n` items
- Total: O(n)

### When to use
- Simple to understand
- Useful for learning, but not ideal for large inputs

---

## 2) Frequency Counting Approach

### Idea
- If lengths differ, return `False`.
- Count the characters in the first string using a dictionary.
- For each character in the second string:
  - If it is not present, return `False`
  - If the count becomes negative or the character is missing, return `False`
- If all counts match, return `True`

### Python Example
```python
def valid_anagrams_frequency_counting(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    char_count = {}
    for char in str_1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in str_2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    return True
```

### Time Complexity
- Building the frequency map: O(n)
- Checking against the second string: O(n)
- Total: O(n)

### Space Complexity
- Dictionary stores at most the number of unique characters
- Worst case: O(n)

### When to use
- Best practical solution for this problem
- Works efficiently for large strings

---

## Comparison

| Approach | Time Complexity | Space Complexity | Notes |
| --- | --- | --- | --- |
| Brute Force | O(n^2) | O(n) | Easy to understand, slower |
| Frequency Counting | O(n) | O(n) | Efficient and recommended |

## Best Solution
The frequency counting approach is the preferred method because it reduces repeated searching and provides linear runtime.

## Example Test Cases
```python
cases = [
    ("listen", "silent", True),
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("a", "a", True),
    ("", "", True),
    ("ab", "a", False),
    ("aacc", "ccaa", True),
    ("abca", "abdc", False),
    ("leetcode", "codeleet", True),
]
```

These are common LeetCode-style edge cases covering valid and invalid anagrams.

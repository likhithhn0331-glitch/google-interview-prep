# Group Anagrams - Notes

## 1. Problem
Given an array of strings `strs`, group all anagrams together.

Example:

```python
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

One valid output:

```python
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

Two strings are anagrams if they contain the same characters with the same frequencies, even if the order differs.

---

## 2. Pattern
This is a hashing problem.

Pattern type:
- Hash map + canonical representation

The key idea is to convert each string into a representation that is identical for all anagrams, then group by that representation.

---

## 3. Recognition Clues
Look for these clues:
- You need to group equivalent items together.
- Items differ by order, not by actual contents.
- You need a single key for each group.
- Anagrams share the same character frequencies.

This suggests:
- sorting each string, or
- counting character frequencies, and then
- storing results in a hash map.

---

## 4. Brute Force
A simple brute force solution is:
- Pick a string.
- Compare it with every later string.
- If they are anagrams, place them in the same group.
- Mark used strings to avoid duplicates.

Example idea:

```python
for i in range(len(strs)):
    if visited[i]:
        continue
    group = [strs[i]]
    for j in range(i + 1, len(strs)):
        if not visited[j] and sorted(strs[i]) == sorted(strs[j]):
            group.append(strs[j])
            visited[j] = True
    result.append(group)
```

This works conceptually but is slow.

---

## 5. Brute-force Complexity
Let:
- `n` = number of strings
- `k` = average string length

For each string, sorting takes `O(k log k)`, and pairwise comparisons lead to `O(n^2)` comparisons in the worst case.

Overall:

```text
Time: O(n^2 * k log k)
Space: O(n)
```

This is not efficient for large input sizes.

---

## 6. Optimized Intuition
The core optimization is:

> Convert every string to a canonical form that is identical for all anagrams.

Then you can group by that canonical form in a hash map.

Examples:
- `eat`, `tea`, `ate` -> `aet`
- `tan`, `nat` -> `ant`

This reduces the problem from comparing many strings to simply mapping signatures to groups.

---

## 7. Invariant
The invariant is:

> Every string in the same hash bucket has the same canonical signature, and therefore the same anagram class.

At any step of the algorithm:
- each processed string is assigned to its correct group
- no string is placed in two groups
- all strings with the same key are in the same bucket

This invariant ensures correctness.

---

## 8. Algorithm
### Option A: Sort-based canonical representation
1. For each string `s`:
   - compute `key = ''.join(sorted(s))`
2. Store `s` in `map[key]`
3. Return the values of the map

Example:

```python
from collections import defaultdict

res = defaultdict(list)
for s in strs:
    res[''.join(sorted(s))].append(s)
return list(res.values())
```

### Option B: Frequency-count based signature
1. For each string, create a count array (for lowercase letters).
2. Use the tuple of counts as the key.
3. Append the string to the appropriate bucket.

Example:

```python
from collections import defaultdict

res = defaultdict(list)
for s in strs:
    counts = [0] * 26
    for ch in s:
        counts[ord(ch) - ord('a')] += 1
    res[tuple(counts)].append(s)
return list(res.values())
```

This is usually the most efficient for lowercase English letters.

---

## 9. Complexity
### Sort-based approach
Let `k` be the average string length.

```text
Time: O(L log k) or O(n * k log k) in aggregate
Space: O(L)
```

Where `L` is the total number of characters across all strings.

### Frequency-count approach
For lowercase English strings:

```text
Time: O(L)
Space: O(L)
```

This is generally faster because it avoids repeated sorting.

---

## 10. Edge Cases
- Empty string: `""` is an anagram of itself
  - Example: `[""]` -> `[[""]]`
- Single-character strings: `["a"]` -> `[["a"]]`
- Duplicate strings: `["a", "a", "a"]` should remain in one group with all three entries
- Strings of different lengths but same letters are not anagrams
- Mixed-case input if case-insensitive matching is required
- Non-lowercase alphabet strings

---

## 11. Common Mistakes
- Comparing strings without canonicalization
- Forgetting to preserve duplicates
- Using a set instead of a list for grouped values
- Using a fixed 26-length array when input may include uppercase, spaces, or punctuation
- Forgetting to normalize case before counting
- Overlooking empty strings

---

## 12. Alternative Approach
Another valid alternative is:

```python
from collections import defaultdict

def group_anagrams_alt(strs):
    groups = defaultdict(list)
    for s in strs:
        groups[tuple(sorted(s))].append(s)
    return list(groups.values())
```

This is conceptually simple and often easier to explain in interviews.

The tradeoff:
- easier to understand
- slightly slower than counting approach for large inputs

---

## 13. Google Follow-ups
### Follow-up 1: Why not compare every pair?
Because that is `O(n^2)` comparisons and does not scale.

### Follow-up 2: What is the canonical key?
A sorted string or a frequency signature.

### Follow-up 3: What if input contains Unicode or uppercase letters?
Use a dictionary-based frequency map instead of a fixed-size array.

### Follow-up 4: What if strings are very large?
A frequency-count approach is still efficient because it processes each string once.

### Follow-up 5: How do you preserve duplicates?
Do not use sets for values; use lists and append all matching strings.

### Follow-up 6: Can you prove correctness?
If two strings are anagrams, they have identical sorted order or identical frequency arrays. Therefore they map to the same key. Conversely, same key implies same character counts, so strings are anagrams.

### Follow-up 7: What is the ideal interview solution?
The most interview-friendly answer is:
- Use a dictionary
- canonical key = sorted string or frequency tuple
- group by key
- return grouped values

This is both efficient and easy to explain.

---

## Quick Interview Summary
- Problem: group anagrams
- Pattern: hashing / canonical representation
- Key idea: all anagrams share the same signature
- Best approach: map signature -> list of strings
- Complexity: `O(L)` with frequency counting for lowercase English strings

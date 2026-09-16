# Group Anagrams - Solution Guide

## Problem
Given an array of strings `strs`, group the anagrams together.

Example:

```python
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

One valid output:

```python
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

The order of groups and strings inside each group does not matter.

---

## 1) Brute Force Solution

File: `brute_force.py`

### Idea
Compare each string against all the strings that come after it. If two strings have the same sorted form, they are anagrams and belong to the same group.

### Logic
- Keep a `visited` list to avoid reusing strings.
- For each unvisited string, create a new group.
- Compare it with later strings.
- If `sorted(strs[i]) == sorted(strs[j])`, put `strs[j]` in the same group.
- Mark `j` as visited.

### Python Code

```python
def group_anagrams_brute_force(strs):
    result = []
    visited = [False] * len(strs)

    for i in range(len(strs)):
        if visited[i]:
            continue
        current_group = [strs[i]]
        visited[i] = True

        for j in range(i + 1, len(strs)):
            if not visited[j] and sorted(strs[i]) == sorted(strs[j]):
                current_group.append(strs[j])
                visited[j] = True

        result.append(current_group)

    return result
```

### Why it works
Two strings are anagrams if they have exactly the same letters in the same counts. Sorting both strings gives the same canonical representation. For example:

- `eat` -> `aet`
- `tea` -> `aet`
- `ate` -> `aet`

So they belong in the same group.

### Strengths
- Very easy to understand.
- Good for explaining the concept of anagram grouping.

### Weaknesses
- Repeated sorting is expensive.
- Compares strings unnecessarily.

---

## 2) Hashing / Frequency Key Solution

File: `hashing_interval.py`

### Idea
Instead of sorting every string repeatedly, build a signature for each string based on character counts. Anagrams will produce the same signature.

### Logic
- Use a dictionary (`defaultdict(list)`).
- For each string, create a frequency array of size 26.
- Count each lowercase letter.
- Convert the count array to a tuple and use it as the hash key.
- Append the string to the list for that signature.
- Return all grouped values from the dictionary.

### Python Code

```python
from collections import defaultdict

def group_anagrams_hashing_interval(strs):
    anagram_map = defaultdict(list)

    for s in strs:
        char_count = [0] * 26
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        key = tuple(char_count)
        anagram_map[key].append(s)

    return list(anagram_map.values())
```

### Why it works
If two strings are anagrams, they contain the same letters with the same frequencies. So their count arrays are identical. That count array becomes the same hash key, grouping them together.

Example:

- `eat` -> `[1, 1, 1, 0, ...]`
- `tea` -> `[1, 1, 1, 0, ...]`
- `ate` -> `[1, 1, 1, 0, ...]`

All map to the same key.

### Strengths
- Much faster than repeated sorting.
- Best fit for interview problems requiring scalable grouping logic.

### Weaknesses
- Assumes input is lowercase English letters only.
- If the problem includes uppercase or non-letter characters, the frequency strategy must be adapted.

---

## 3) Comparison of Both Solutions

### Brute Force
- Uses repeated sorting comparisons.
- Easy to reason about but inefficient.
- Best for demonstrating the core concept, not for large inputs.

### Hashing Approach
- Builds a canonical representation using character counts.
- Groups strings by signature in one pass.
- Much more efficient and suitable for production-quality solutions.

### In One Line
The brute force solution checks pairwise comparisons, while the hashing solution converts each string to a signature and groups by that signature.

---

## 4) Time and Space Complexity

Let:
- `n` = number of strings
- `k` = average length of a string
- `L` = total characters across all strings

### Brute Force
For each string, it sorts and compares against others.

- Sorting each string: `O(k log k)`
- Worst-case comparisons: `O(n^2)`
- Total: `O(n^2 * k log k)`

Space:
- `O(n)` for visited and result groups

### Hashing Approach
For each string, we count letters in a fixed-size array of 26 slots.

- Counting characters: `O(k)` per string
- Across all strings: `O(L)`
- Dictionary insertion/grouping: `O(n)` amortized

Total:
- Time: `O(L)` for lowercase English letters
- Space: `O(L)` for stored grouped strings and count keys

### Why hashing is better
Because it avoids repeated sorting and unnecessary pairwise comparisons. It reduces the problem to conversion to a canonical key and dictionary lookup.

---

## 5) Interview Discussion Points

### Core concept
This problem tests:
- Hash map usage
- Canonical representation
- Grouping equivalent elements by a shared key

### Typical follow-up question
Why not compare every pair of strings directly?

Answer:
- It is too slow for large inputs.
- A canonical key reduces the problem to constant-time lookups per string.

### Another follow-up
What if strings can contain uppercase letters, spaces, or punctuation?

Answer:
- Use a frequency map/dictionary instead of a fixed-size 26-length array.
- Example: `Counter(s)` in Python.

### Another follow-up
What if input strings are very large?

Answer:
- The hashing approach remains efficient because it only counts characters once per string.
- It avoids repeated sorting of large strings.

---

## 6) Interview Questions with Answers

### Basic Questions

1. What makes two strings anagrams?
   - Two strings are anagrams if they have the same characters with the same frequencies, regardless of order.
   - Example: `eat`, `tea`, and `ate` are anagrams.

2. How would you group all anagrams in a list of strings?
   - Build a canonical key for each string, such as its sorted version or frequency array.
   - Use a hash map where the key is the canonical representation and the value is a list of grouped strings.

3. Why is sorting a useful canonical representation here?
   - Sorting ensures that all anagrams produce the same string, like `eat -> aet`, `tea -> aet`, `ate -> aet`.
   - This gives a uniform key for grouping.

4. What is the difference between brute force and hashing-based grouping?
   - Brute force compares every string with every other string.
   - Hashing builds one signature per string and groups by that signature, which is far more efficient.

### Intermediate Questions

5. Why is a hash map a good fit for this problem?
   - Hash maps allow constant-time lookups by a key.
   - We can map each canonical signature to a list of strings that share that pattern.

6. What is the time complexity of sorting-based grouping?
   - For each string, sorting is `O(k log k)`, and if done for all pairs in a naive way, it becomes `O(n^2 * k log k)` in the worst case.
   - So it is not scalable for large input sizes.

7. How can you optimize grouping without comparing every pair of strings?
   - Convert each string into a canonical signature once.
   - Store it in a dictionary keyed by that signature.
   - Append the original string to the matching bucket.

8. What is the canonical representation for an anagram group?
   - A common choice is the sorted string, such as `eat -> aet` and `tea -> aet`.
   - Another is a character-frequency array, like `[1,1,1,0,...]` for lowercase English letters.

### Advanced Questions

9. How would you adapt the solution for arbitrary Unicode strings?
   - Use a dictionary or `Counter` instead of a fixed 26-size array.
   - For example, `Counter(s)` counts characters of any type, not just lowercase English letters.

10. What if the input contains duplicate strings? How do you preserve them?
   - The grouping should preserve every occurrence.
   - A dictionary value list naturally stores duplicates, so `['a', 'a', 'a']` stays in one group.

11. What if the strings contain uppercase and lowercase letters treated as the same character?
   - Normalize the input first, such as converting all to lowercase or a common case.
   - Then build the signature on the normalized version.

12. Could you solve the problem using a trie or a frequency map instead of sorting?
   - Yes.
   - A frequency map (`Counter`) is a standard alternative to sorting, especially for fixed alphabets.
   - A trie is not the usual choice here because the problem is about grouping by character counts, not prefix matching.

---

## Final Takeaway
For this problem, the optimal pattern is:

```text
String -> Canonical signature -> Hash map -> Grouped anagrams
```

The hashing/frequency approach is the standard interview solution because it is much faster and scales better than brute force.

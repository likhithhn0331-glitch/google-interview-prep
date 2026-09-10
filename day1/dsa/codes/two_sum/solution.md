# Two Sum Solutions

## Problem
Given an array of integers `nums` and a target integer `target`, find two distinct indices `i` and `j` such that:

`nums[i] + nums[j] == target`

Return the indices of the two numbers.

---

## 1) Brute Force

### Idea
Check every pair of elements and compare their sum with the target.

### Python Example
```python
def two_sum_bf(array, target):
    n = len(array)
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] + array[j] == target:
                return [i, j]
    return None
```

### Why it works
Every possible pair is checked once. If a valid pair exists, it will be found.

### Complexity
- Time: O(n^2)
- Space: O(1)

This is the simplest approach, but it is slow for large arrays.

---

## 2) Hash Map / Dictionary

### Idea
For each number, compute its complement:

`complement = target - current_number`

If the complement has already been seen in a hash map, then the pair is found.

### Python Example
```python
def two_sum_hashmap(array, target):
    num_to_index = {}

    for i, num in enumerate(array):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

    return None
```

### Why it works
Every element is processed once. When we reach a number `x`, we only need to know whether `target - x` was seen earlier. If it was, then those two numbers add up to the target.

### Complexity
- Time: O(n) average case
- Space: O(n)

This is the best general-purpose solution for the problem.

---

## 3) Two Pointers (after sorting)

### Idea
Create a list of `(value, original_index)` pairs, sort it by value, then use two pointers from both ends of the sorted array.

### Python Example
```python
def two_sum_two_pointer(array, target):
    indexed_array = [(array[i], i) for i in range(len(array))]
    indexed_array.sort()

    left = 0
    right = len(indexed_array) - 1

    while left < right:
        current_sum = indexed_array[left][0] + indexed_array[right][0]
        if current_sum == target:
            return [indexed_array[left][1], indexed_array[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None
```

### Why it works
After sorting, the sum of the leftmost and rightmost values tells us whether we need a larger or smaller value. Moving the pointers shrinks the search range until the target is found or no solution remains.

### Complexity
- Time: O(n log n) because of sorting
- Space: O(n) because of the sorted list of pairs

This is efficient when sorting is acceptable, but it is not as fast as the hash map approach for this problem.

---

## Summary

| Approach | Time Complexity | Space Complexity |
| --- | --- | --- |
| Brute Force | O(n^2) | O(1) |
| Hash Map | O(n) average | O(n) |
| Two Pointers (sorted) | O(n log n) | O(n) |

The hash map solution is usually the best choice for Two Sum because it runs in linear time on average.

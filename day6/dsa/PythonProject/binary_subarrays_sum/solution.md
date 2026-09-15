# Binary Subarrays With Sum

## 1) Brute Force Solution

The simplest way to solve this is to check every possible subarray.

For each starting index `left`, we extend `right` from `left` to the end of the array and maintain a running sum.

If the running sum equals `goal`, we count that subarray.

Python implementation:

```python
def brute_force_count(nums, goal):
    count = 0
    n = len(nums)

    for left in range(n):
        current_sum = 0
        for right in range(left, n):
            current_sum += nums[right]
            if current_sum == goal:
                count += 1

    return count
```

### Why this works
A subarray is defined by a start and end index. The brute-force method checks each possible pair `(left, right)` and counts it if its sum equals the target value.

### Complexity
- Time complexity: `O(n^2)`
  - There are `O(n^2)` subarrays in total.
- Space complexity: `O(1)`
  - We only keep a running sum and a counter.

### When to use it
This is useful for understanding the problem clearly, but it becomes too slow for large inputs (`n` up to `10^5`).

---

## 2) Optimized Solution Using Prefix Sums

### Key idea
Let `prefix_sum[i]` be the sum of the first `i` elements.

Then the sum of a subarray from `l` to `r` is:

```text
prefix_sum[r + 1] - prefix_sum[l]
```

If this equals `goal`, then:

```text
prefix_sum[r + 1] = prefix_sum[l] + goal
```

So while scanning the array, we can count how many times a previous prefix sum equal to `current_prefix_sum - goal` has appeared.

Python implementation:

```python
from collections import defaultdict


def prefix_sum_count(nums, goal):
    prefix_sum = 0
    count = 0
    freq = defaultdict(int)
    freq[0] = 1

    for num in nums:
        prefix_sum += num
        count += freq.get(prefix_sum - goal, 0)
        freq[prefix_sum] += 1

    return count
```

### Why this works
When we reach a current prefix sum `S`, any earlier prefix sum `S - goal` tells us there was a subarray ending here whose sum is `goal`.

Formally:

```text
current_prefix_sum - previous_prefix_sum = goal
```

That means the subarray between those two points sums to `goal`, so we count it.

### Complexity
- Time complexity: `O(n)`
  - Each element is processed once.
- Space complexity: `O(n)`
  - In the worst case, all prefix sums are distinct and stored in the map.

---

## 3) Comparison of Both Solutions

| Approach | Idea | Time Complexity | Space Complexity | Best for |
|---|---|---:|---:|---|
| Brute force | Check all subarrays | `O(n^2)` | `O(1)` | Small inputs / explanation |
| Prefix sums | Count matching prefix-sum differences | `O(n)` | `O(n)` | Large inputs / interviews |

### Why the optimized solution is preferred
The brute-force method is easy to understand but too slow for large arrays.
The prefix-sum approach compresses repeated work and transforms the problem into a frequency-count task, which is ideal for interview settings and production code.

---

## 4) Time and Space Complexity Explanation

### Brute-force explanation
For each starting index, the algorithm may scan up to `n` elements.

So total work is:

```text
n + (n-1) + (n-2) + ... + 1 = O(n^2)
```

This is quadratic time because the algorithm does repeated work.

### Prefix-sum explanation
Each iteration does:
- one addition to the running prefix sum
- one map lookup
- one map update

All of these are constant-time on average in Python dictionaries.

So the total is:

```text
O(n)
```

Space is `O(n)` because the frequency map stores prefix sums that appear during the pass.

---

## 5) Interview Questions to Practice

### Basic understanding
1. What is the difference between a subarray and a subsequence?
2. Why is prefix sum useful for subarray-sum problems?
3. How does a frequency map help in counting valid subarrays?

### Variations
4. What if the array contains negative numbers?
5. How would you modify the solution if you had to count subarrays with sum greater than `goal`?
6. What if the problem asked for the number of subarrays whose sum equals `k`, not necessarily with binary numbers?
7. Can you solve the same problem using a sliding window when the array is non-negative?

### Trickier questions
8. How would you prove the prefix-sum formula?
9. Why does the frequency map start with `{0: 1}`?
10. What happens if `goal` is `0`?
11. Can you explain the time and space complexity with a small example?
12. Could there be integer overflow issues in other languages? How would you handle them?

### Coding challenge prompts
13. Write the brute-force and optimized versions side by side.
14. Given a binary array, explain why each `1` contributes to many different subarrays.
15. Walk through the algorithm for `nums = [1, 0, 1, 0, 1]` and `goal = 2`.

---

## Summary

The brute-force method is conceptually simple but slow (`O(n^2)`).
The prefix-sum frequency method is the standard interview solution for this problem and runs in `O(n)` time.

This is a classic example of reducing repeated computations using a mathematical pattern instead of checking every subarray individually.

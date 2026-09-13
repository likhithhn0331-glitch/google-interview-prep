# Solution: Maximum Average Subarray I

## Problem Restatement

Given an array of numbers and a fixed window size `k`, find the maximum average of any contiguous subarray of length `k`.

Example:

```text
array = [1, 12, -5, -6, 50, 3]
k = 4
```

The valid windows are:

- `[1, 12, -5, -6]` -> average = `0.5`
- `[12, -5, -6, 50]` -> average = `12.75`
- `[-5, -6, 50, 3]` -> average = `10.5`

Answer: `12.75`

---

## 1) Brute Force Solution

### Idea

Try every valid subarray of length `k`.

For each starting index `i`, compute the sum of `array[i : i + k]` and divide by `k`.

Keep track of the maximum average seen so far.

### Python Code

```python
def max_average_brute_force(array, k):
    n = len(array)
    if k <= 0 or k > n:
        return None

    max_avg = float('-inf')
    for i in range(n - k + 1):
        current_sum = sum(array[i:i + k])
        current_avg = current_sum / k
        if current_avg > max_avg:
            max_avg = current_avg
    return max_avg
```

### How it works

- The outer loop picks each possible start of the window.
- The inner step sums that window.
- Because the size is fixed, every average is computed as:

```text
window_sum / k
```

- We compare each average and store the largest one.

### Example

For:

```text
[1, 12, -5, -6, 50, 3], k = 4
```

The brute force method checks:

- `[1, 12, -5, -6]` -> `0.5`
- `[12, -5, -6, 50]` -> `12.75`
- `[-5, -6, 50, 3]` -> `10.5`

Hence, maximum is `12.75`.

### Pros

- Very easy to understand.
- Simple to implement.
- Good for teaching the core idea.

### Cons

- Recomputes the sum for each window from scratch.
- Too slow for large arrays.

---

## 2) Sliding Window Solution

### Idea

Use a moving window of fixed length `k`.

Instead of recalculating the sum for every subarray, keep a running sum:

- first window sum = sum of first `k` elements
- for each next window:
  - subtract the element leaving the window
  - add the element entering the window

This works because adjacent windows share almost all elements.

### Python Code

```python
def max_average_sliding_window(array, k):
    n = len(array)
    if k <= 0 or k > n:
        return None

    current_sum = sum(array[:k])
    max_avg = current_sum / k

    for i in range(k, n):
        current_sum += array[i] - array[i - k]
        current_avg = current_sum / k
        if current_avg > max_avg:
            max_avg = current_avg

    return max_avg
```

### How it works

1. Compute the sum of the first `k` elements.
2. Treat that as the starting maximum average.
3. For every next index `i`:

```text
new_sum = old_sum - array[i-k] + array[i]
```

4. Recompute the average for the new window and update the result if it is larger.

### Example

```text
array = [1, 12, -5, -6, 50, 3]
k = 4
```

Initial window:

```text
[1, 12, -5, -6]
```

Sum = `2`, average = `0.5`

Next window:

```text
[12, -5, -6, 50]
```

Update:

```text
2 - 1 + 50 = 51
```

Average = `51 / 4 = 12.75`

Next window:

```text
[-5, -6, 50, 3]
```

Update:

```text
51 - 12 + 3 = 42
```

Average = `42 / 4 = 10.5`

Best result remains `12.75`.

### Pros

- Extremely efficient.
- Processes the array in one pass after the first window.
- Great for large inputs.

### Cons

- Slightly less intuitive at first glance.
- Requires understanding how adjacent windows overlap.

---

## 3) Comparing Both Solutions

| Method | Idea | Time Complexity | Space Complexity | Best Use |
|---|---|---:|---:|---|
| Brute Force | Check every window separately | `O(n * k)` | `O(1)` | Small inputs, understanding the problem |
| Sliding Window | Reuse previous window sum | `O(n)` | `O(1)` | Large inputs, interviews, production code |

### Key difference

The brute-force solution recomputes the sum of each window from scratch.

The sliding window solution uses the fact that each window is almost the same as the previous one, so it updates the sum in constant time.

This is the main optimization that turns an inefficient solution into an optimal one.

---

## 4) Time and Space Complexity Explanation

### Brute Force Complexity

There are `n - k + 1` valid windows.

For each window, we compute its sum using `sum(array[i:i+k])`.

That sum takes `O(k)` time.

So total time is:

```text
O((n - k + 1) * k)
```

which is roughly:

```text
O(n * k)
```

Space complexity is:

```text
O(1)
```

because we use only a few variables.

### Sliding Window Complexity

- First window sum: `O(k)`
- Each next window update: `O(1)`
- Total across the array: `O(n)`

So the overall time complexity is:

```text
O(n)
```

Space complexity is:

```text
O(1)
```

because we keep only the current sum and a few counters.

This is optimal for this problem because every element has to be considered at least once.

---

## 5) Interview Questions to Practice

### Concept questions

1. What is the difference between a brute-force approach and an optimized sliding window approach?
2. Why does the sliding window work for fixed-length subarrays?
3. Why is maximizing the average equivalent to maximizing the sum when `k` is constant?
4. How do adjacent windows overlap, and why is that important?

### Coding questions

1. Write the brute-force version from scratch.
2. Rewrite the same solution using the sliding window technique.
3. Handle edge cases like:
   - `k == 1`
   - `k == n`
   - negative numbers
   - `k > n`
4. Explain why the sliding window is `O(n)` and not `O(n * k)`.

### Follow-up questions

1. Can this be solved using prefix sums?
2. What if the window size were not fixed?
3. What if you had to return the actual subarray and not just the maximum average?
4. Can you explain the tradeoff between clarity and optimization in interviews?

---

## Final Takeaway

The best solution is the sliding window approach because it uses the overlap between adjacent windows to avoid repeated work.

- Brute force: easy to understand, but too slow for large inputs
- Sliding window: efficient, elegant, and the standard interview solution

If you understand why the sum can be updated as:

```text
new_sum = old_sum - leaving_element + entering_element
```

you understand the heart of this problem.

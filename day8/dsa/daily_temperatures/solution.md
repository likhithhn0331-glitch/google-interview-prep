# Daily Temperatures

## Problem

Given an array of daily temperatures, return an array `answer` where `answer[i]` is the number of days you must wait after day `i` to get a warmer temperature. If there is no warmer day later, the value is `0`.

Example:

- Input: `[73, 74, 75, 71, 69, 72, 76, 73]`
- Output: `[1, 1, 4, 2, 1, 1, 0, 0]`

## Brute Force Approach

The simplest solution is to check every future day for each index.

Algorithm:

1. For each day `i`, start checking `j = i + 1`.
2. If `temperatures[j] > temperatures[i]`, then the answer is `j - i`.
3. If no warmer temperature exists, keep `0`.

Pseudo-code:

```python
answer = [0] * n
for i in range(n):
    for j in range(i + 1, n):
        if temperatures[j] > temperatures[i]:
            answer[i] = j - i
            break
```

### Complexity

- Time: `O(n^2)`
- Space: `O(1)` extra space, aside from the output array

This is easy to understand, but inefficient for large inputs.

## Stack-Based Optimal Solution

Use a monotonic decreasing stack of indices.

Key idea:

- Maintain a stack of indices whose temperatures are in decreasing order.
- When the current temperature is greater than the temperature at the top of the stack,
  the top index has found a warmer future day.
- Compute the waiting days as `current_index - popped_index`.
- Continue popping while the current temperature is warmer.
- Push the current index onto the stack.

Pseudo-code:

```python
stack = []
answer = [0] * n

for i, temp in enumerate(temperatures):
    while stack and temp > temperatures[stack[-1]]:
        previous_index = stack.pop()
        answer[previous_index] = i - previous_index
    stack.append(i)
```

### Why it works

The stack always stores temperatures that have not yet found a warmer day. As soon as a warmer temperature appears, it resolves all earlier smaller temperatures at the top of the stack.

### Complexity

- Time: `O(n)`
- Space: `O(n)`

This is the standard efficient solution for this problem.

## Interview Notes

### Brute force interview answer

A candidate can explain that the naive method is straightforward but does not scale for large arrays because each index potentially scans the entire suffix.

### Stack interview answer

An interviewer will often expect the monotonic decreasing stack pattern. This is a strong signal that you can recognize a problem where a stack can convert repeated comparisons into linear-time work.

## Possible Interview Questions and Answers

### Q1: Why is the brute-force solution not good enough?

Answer:

The brute-force solution checks every future day for each index. In the worst case, that's `n * (n-1) / 2` comparisons, which is `O(n^2)`. For arrays with length up to `10^5`, this is too slow and can exceed time limits.

### Q2: What is the main idea behind the stack solution?

Answer:

We maintain a stack of indices with temperatures in decreasing order. When the current temperature is warmer than the temperature at the top of the stack, that earlier day has found its next warmer day. We calculate the difference in indices and pop the stack until the order is valid again.

### Q3: Why does the stack remain monotonic?

Answer:

Because we only push the current index after processing all warmer temperatures. If the current temperature is warmer than the top, we pop the top and resolve it. This keeps the stack in decreasing temperature order, so the top is always the most recent candidate that may still need a warmer future day.

### Q4: How do we calculate the answer for each day?

Answer:

When we find a warmer temperature at index `i` and a previous index `j` is popped from the stack, the waiting days are `i - j`. We store that in `answer[j]`.

### Q5: What is the time complexity of the optimal solution?

Answer:

Each index is pushed onto the stack once and popped at most once. So the total work is linear in the number of elements: `O(n)`.

### Q6: What is the space complexity?

Answer:

The stack can hold up to `n` indices in the worst case, so the space complexity is `O(n)`.

### Q7: What if there is no warmer day in the future?

Answer:

Then that index will never be popped, so its answer remains `0`.

### Q8: Could this be solved in any other way?

Answer:

Yes, the brute force method is the direct way, but it is too slow for larger inputs. The monotonic stack is the standard efficient approach because it reuses information from previously seen temperatures and avoids repeated scanning.

## Summary

- Brute force: easy but `O(n^2)`.
- Stack solution: elegant and optimal with `O(n)` time.
- The stack approach is the preferred solution in coding interviews.

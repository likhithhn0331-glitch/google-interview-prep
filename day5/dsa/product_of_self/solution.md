# Solution Guide: Product of Array Except Self

## Problem Recap

We are given an integer array `nums` and need to return an array `answer` such that:

```python
answer[i] = product of all nums[j] for j != i
```

The challenge is to do this efficiently without using division, and ideally in linear time.

The two main ways to think about the problem are:

1. Brute force multiplication for each index
2. Prefix + suffix product strategy

---

## Solution 1: Brute Force

### Idea

For each index `i`, multiply every element except `nums[i]`.

This is the most straightforward approach and is easy to reason about.

### Python Implementation

```python
def product_except_self_brute_force(nums):
    n = len(nums)
    result = [0] * n

    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result[i] = product

    return result
```

### Why it works

At each index `i`, the inner loop multiplies all elements except the one at that index. So every output element is computed exactly as required.

### Complexity

- Time complexity: `O(n^2)`
  - Outer loop: `n`
  - Inner loop: up to `n`
  - Total: `n * n = O(n^2)`
- Space complexity: `O(1)` extra space
  - We only store a few variables like `product` and loop indices.
  - The returned array is required output, so it is not counted as extra space in many interview definitions.

### When to use it

- When you are learning the problem
- For very small inputs
- As a baseline before optimizing

### Limitation

This is too slow for large arrays because each index recalculates the full product from scratch.

---

## Solution 2: Prefix and Suffix Products

### Idea

Instead of recomputing everything for each index, compute products of all elements to the left and right of each position.

For every index `i`:

```text
left[i] = product of nums[0..i-1]
right[i] = product of nums[i+1..n-1]
answer[i] = left[i] * right[i]
```

### Python Implementation

```python
def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    # Build prefix products in answer
    for i in range(1, n):
        answer[i] = answer[i - 1] * nums[i - 1]

    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer
```

### Why it works

- After the first loop, `answer[i]` stores the product of all numbers before index `i`.
- `suffix` stores the product of all numbers to the right of the current index as we move from right to left.
- Multiplying them gives the product of every element except `nums[i]`.

This works because each value is included exactly once in the correct left or right product.

### Complexity

- Time complexity: `O(n)`
  - One left-to-right pass
  - One right-to-left pass
- Space complexity: `O(1)` extra space
  - We use only a few variables like `suffix`
  - The output array is allowed by the problem requirement

### Why this is the preferred solution

This is the standard interview solution because it:

- runs in linear time
- avoids division entirely
- handles zero values correctly
- uses only constant extra memory beyond the result array

---

## Comparing Both Solutions

### Brute Force

Pros:

- Easy to understand
- Straightforward logic
- Good as a baseline or for small inputs

Cons:

- `O(n^2)` time
- Repeats the same multiplication work many times
- Not acceptable for large arrays

### Prefix + Suffix Products

Pros:

- `O(n)` time
- `O(1)` extra space
- Elegant and interview-friendly
- Works without division and handles zeros cleanly

Cons:

- Slightly harder to reason about at first
- Requires understanding of left/right product composition

### Which one is better?

The prefix + suffix approach is the correct interview answer for this problem because it satisfies the required constraints and demonstrates strong optimization thinking.

---

## Time and Space Complexity Explanation

### 1. Brute Force

For every index `i`, we scan the entire array again to ignore `nums[i]`.

- There are `n` possible values of `i`
- For each one, we process up to `n` elements
- Total work: `n * n = O(n^2)`

Memory is constant because we only keep a running `product` and a few loop variables.

### 2. Prefix + Suffix Products

We do two linear passes over the array.

- Left pass: compute left-side products
- Right pass: multiply by suffix products

Each element is handled a constant number of times, so total work is `O(n)`.

Space:

- The output array requires `O(n)` space because the problem demands returning a result array.
- Extra working memory besides the result is `O(1)`.

This makes it optimal under the problem constraints.

---

## Interview Follow-up Questions

Here are some good interview-style questions to ask around this problem:

1. Can you solve it without using division?
   - The prefix/suffix method is the key answer.

2. What happens when the array contains zero?
   - If a zero exists, then the product except at that zero index is the product of all non-zero values, while the zero index itself becomes `0` if there are any other non-zero terms.

3. Can this be done in-place besides the output array?
   - Yes, the result array is usually the storage for the final answer, but you can still use a small amount of extra state.

4. Why is the brute-force solution not acceptable for large inputs?
   - Because it recomputes the same multiplications repeatedly and reaches `O(n^2)`.

5. How would you explain the prefix/suffix idea in one sentence?
   - "Each answer value is the product of all numbers left of the current index times all numbers right of the current index."

6. What is the difference between extra space and required output space?
   - The problem allows the output array itself, so extra working memory can still be constant.

7. Can you adapt this idea to a similar problem like product of subarrays or prefix products?
   - Yes, the same left/right accumulation idea is a common pattern in array problems.

8. What if the array contains negative numbers?
   - The method still works, because it only relies on multiplication and accumulation, not sign-specific logic.

---

## Final Takeaway

The best solution is the prefix + suffix product method.

- It is efficient: `O(n)` time
- It is memory-aware: `O(1)` extra space
- It is a classic interview pattern for problems where you need to avoid repeated recomputation

If you are preparing for interviews, this is the solution you should be able to explain clearly and confidently.

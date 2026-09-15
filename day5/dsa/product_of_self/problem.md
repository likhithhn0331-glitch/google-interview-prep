# DSA PROBLEM 2 — Product of Array Except Self

## Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The solution must satisfy the following constraints:

- Time complexity: `O(n)`
- Space complexity: `O(1)` extra space (excluding the output array)

## Example

```python
nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
```

### Explanation

- For index `0`: product of all elements except `nums[0]` = `2 * 3 * 4 = 24`
- For index `1`: product of all elements except `nums[1]` = `1 * 3 * 4 = 12`
- For index `2`: product of all elements except `nums[2]` = `1 * 2 * 4 = 8`
- For index `3`: product of all elements except `nums[3]` = `1 * 2 * 3 = 6`

## Key Insight: Prefix and Suffix Products

A naive approach would multiply the entire array for each index, which is `O(n^2)`.

Instead, compute:

- left product: product of all elements to the left of each index
- right product: product of all elements to the right of each index

Then:

```text
answer[i] = left[i] * right[i]
```

This avoids repeated multiplication and keeps the runtime linear.

## Efficient Idea

Use a single output array to store prefix products, then traverse from right to left while maintaining a running suffix product.

### Step-by-step

1. Initialize `answer` with length `n`.
2. Set `answer[0] = 1`.
3. Fill `answer[i]` with the product of all values to its left.
4. Traverse from right to left while tracking a `suffix` product.
5. Multiply `answer[i]` by `suffix` and update `suffix *= nums[i]`.

This gives the product of everything except the current element in constant time per index.

## Why This Works

At any index `i`:

- `answer[i]` already contains the product of all elements before `i`
- `suffix` contains the product of all elements after `i`

So the product excluding `nums[i]` is exactly:

```text
prefix[i] * suffix[i]
```

Each element is used in the correct computation exactly once, making the total work linear.

## Algorithm

```python
def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    # prefix products
    for i in range(1, n):
        answer[i] = answer[i - 1] * nums[i - 1]

    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer
```

## Complexity

- Time Complexity: `O(n)`
- Space Complexity: `O(1)` extra space, not counting the output array

## Notes

This is a classic interview problem that tests your ability to avoid brute-force multiplication and instead use prefix/suffix reasoning.

A common follow-up is:

- Can you solve it without using division?
- Can you do it in-place (besides the output array)?

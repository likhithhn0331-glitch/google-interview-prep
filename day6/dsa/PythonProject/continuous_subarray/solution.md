# Solution: Continuous Subarray

## Problem restatement
Given an integer array `nums` and an integer `k`, return `true` if there exists a contiguous subarray of length at least 2 whose sum is a multiple of `k`.

Examples:
- `nums = [23, 2, 4, 6, 7], k = 6` -> `true` because `[2, 4]` sums to `6`
- `nums = [23, 2, 6, 4, 7], k = 6` -> `true` because the whole array sums to `42`
- `nums = [1, 2, 3], k = 5` -> `true` because `[2, 3]` sums to `5`
- `nums = [1, 1], k = 0` -> `false` because no subarray of length >= 2 sums to 0

## 1) Brute-force solution
### Idea
Check every possible contiguous subarray and compute its sum. If the sum is divisible by `k` and the subarray length is at least 2, return `true`.

### Python implementation
```python
def continuous_subarray_brute_force(nums, k):
    n = len(nums)
    for left in range(n):
        current_sum = 0
        for right in range(left, n):
            current_sum += nums[right]
            subarray_length = right - left + 1
            if subarray_length >= 2:
                if k == 0:
                    if current_sum == 0:
                        return True
                elif current_sum % k == 0:
                    return True
    return False
```

### How it works
- Start from each index as the left boundary.
- Extend the right boundary one element at a time.
- Keep adding values to `current_sum`.
- If the running sum is divisible by `k` and the subarray length is at least 2, return `true`.

### Why it works
This checks every valid contiguous subarray. If any subarray satisfies the condition, it will be found.

### Complexity
- Time: `O(n^2)`
- Space: `O(1)`

Reason:
- There are `O(n^2)` subarrays in total.
- Each subarray sum is computed in constant extra space.

## 2) Optimized prefix-sum solution
### Idea
Use prefix sums and remainders modulo `k`.

For a running prefix sum `prefix_sum`, if the same remainder appears again at a different position, the difference between those prefix sums is divisible by `k`.

That difference corresponds to a contiguous subarray whose sum is a multiple of `k`.

### Key observation
For any indices `i` and `j` with `i < j`:
- `prefix[j] - prefix[i]` is the sum of subarray `nums[i:j]`
- If `(prefix[j] % k) == (prefix[i] % k)`, then:
  - `prefix[j] - prefix[i]` is divisible by `k`
  - therefore the subarray sum is divisible by `k`

We also require the subarray length to be at least 2, so we check:
- `j - i >= 2`

### Python implementation
```python
def continuous_subarray_prefix_sum(nums, k):
    prefix_sum = 0
    seen = {0: -1}

    for i, num in enumerate(nums):
        prefix_sum += num

        if k == 0:
            if prefix_sum in seen:
                if i - seen[prefix_sum] >= 2:
                    return True
            else:
                seen[prefix_sum] = i
            continue

        remainder = prefix_sum % k
        if remainder in seen:
            if i - seen[remainder] >= 2:
                return True
        else:
            seen[remainder] = i

    return False
```

### How it works
- Maintain a dictionary `seen` that stores the first index for each remainder (or prefix sum when `k == 0`).
- Each time we update the prefix sum, compute its remainder modulo `k`.
- If that remainder has appeared before, compute the distance between current index and the earlier occurrence.
- If the distance is at least 2, we found a valid subarray.

### Why it works
If two prefix sums have the same remainder modulo `k`, their difference is a multiple of `k`, meaning the subarray between those positions sums to a multiple of `k`.

Because the dictionary stores the first encountered index for each remainder, the first repeated remainder gives us the shortest valid subarray in the process; checking the length ensures the requirement is satisfied.

### Complexity
- Time: `O(n)`
- Space: `O(n)`

Reason:
- Each element is processed once.
- A hash map stores at most one entry per remainder.

## 3) Comparison of both solutions

### Brute force
- Very simple to reason about
- Easy to implement correctly
- Not efficient for large inputs
- Best for small arrays and validation/testing

### Prefix sum
- More elegant and scalable
- Works efficiently for arrays up to `10^5` or more
- Requires careful handling of remainder logic and `k == 0`
- Preferred for interview and production use

### Side-by-side
| Solution | Time | Space | Best for |
|---------|------|-------|----------|
| Brute force | `O(n^2)` | `O(1)` | Small inputs, understanding the problem |
| Prefix sum | `O(n)` | `O(n)` | Large inputs, interview optimization |

## 4) Time and space complexity explanation
### Brute force
We try every left index and every right index.
Number of subarrays is:
- `n + (n-1) + ... + 1 = O(n^2)`
So the runtime is quadratic.
Extra memory is constant because we only store a few variables like `current_sum` and index positions.

### Prefix sum
Each element is visited once. Each operation on the hash map is average `O(1)`.
Thus total runtime is linear: `O(n)`.
The hash map stores remainders or prefix sums; in the worst case it holds at most `n + 1` entries, so space is `O(n)`.

## 5) Interview questions to practice
1. Why is the brute-force method `O(n^2)`?
2. What is the key observation behind prefix sum with modulo arithmetic?
3. How do we handle `k == 0` differently from `k != 0`?
4. Is it possible to return early as soon as we find a valid subarray?
5. What if the array contains negative numbers? Does the prefix-sum method still work?
6. Can the same idea be extended to count subarrays whose sum is divisible by `k` instead of just checking existence?
7. What happens if the subarray length is exactly 1? Why is it invalid?
8. Why do we need to ensure the distance between repeated remainders is at least 2?
9. Can we reduce the space complexity below `O(n)`? Why or why not?
10. How would you explain the prefix-sum approach in a 60-second interview answer?

## 6) Interview-ready summary
The efficient solution uses prefix sums and remainders modulo `k`:
- Track the prefix sum while scanning the array.
- Store the first index seen for each remainder.
- If the same remainder appears again, the subarray between them has sum divisible by `k`.
- Check that its length is at least 2.

This reduces the problem from quadratic time to linear time, which is the standard optimal approach for this task.

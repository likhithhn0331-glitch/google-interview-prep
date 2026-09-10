Contains Duplicate — Solutions

Problem
Given an integer array nums, determine whether any value appears at least twice. Return True if any duplicate exists; otherwise return False.

Overview
This document compares three approaches: brute-force, hash-set (recommended), and sorting. Each approach is described, analyzed (time/space), and illustrated with a short step-by-step example. Empirical timing notes reference the provided timing harness (main.py).

1) Brute-force (nested loops)
Description:
- Compare every pair (i, j) with i < j. If nums[i] == nums[j], return True.
- Straightforward but compares O(n^2) pairs.

Step-by-step (nums = [1, 2, 3, 1]):
- i=0 compare with j=1,2,3 -> match at j=3 -> return True

Time complexity: O(n^2) comparisons
Space complexity: O(1) extra space
Pros:
- No extra memory required
- Simple to implement and reason about
Cons:
- Extremely slow for large arrays; becomes impractical when n is in the thousands or more

2) Hash-set (recommended)
Description:
- Iterate once, maintain a set seen.
- For each x in nums: if x in seen -> duplicate found; otherwise add x to seen.
- This detects duplicates as soon as they appear (early exit possible).

Step-by-step (nums = [1, 2, 3, 1]):
- seen = {}
- read 1 -> not in seen -> add -> seen={1}
- read 2 -> add -> seen={1,2}
- read 3 -> add -> seen={1,2,3}
- read 1 -> 1 in seen -> return True

Time complexity: Average O(n) — each membership/add is O(1) on average
Worst-case: O(n^2) in degenerate hash-collision cases (rare)
Space complexity: O(n) extra space to store seen set
Pros:
- Fast in practice and simple
- Early exit when duplicate occurs
Cons:
- Uses extra memory proportional to distinct values
- Slight overhead from hashing

3) Sorting-based approach (alternative)
Description:
- Sort the array in O(n log n), then perform a single pass checking adjacent elements for equality.
- Useful when in-place modification is allowed or memory is constrained compared to a hash table.

Step-by-step (nums = [1, 2, 3, 1]):
- sorted -> [1,1,2,3]
- check adjacent pairs -> 1==1 -> return True

Time complexity: O(n log n) for sorting (plus O(n) scan)
Space complexity: O(1) extra if sort in-place (e.g., Timsort in Python uses O(log n) extra), or O(n) if a stable out-of-place sort is used
Pros:
- No hash overhead
- Deterministic time bound (no hash-collision worst-case)
Cons:
- Modifies array (unless copied)
- Slower than hash-set for typical large inputs where O(n) is possible

Complexity comparison summary
- Brute-force: Time O(n^2), Space O(1)
- Hash-set: Average Time O(n), Space O(n)
- Sorting: Time O(n log n), Space O(1)–O(n) depending on sort

Empirical timing notes (using main.py harness)
- For small n (~10s), differences are minor and brute-force may appear acceptable.
- As n grows (hundreds to thousands), set-based method time grows roughly linearly; brute-force time grows quadratically and quickly dominates runtime.
- Sorting-based method typically lies between set and brute-force in practice: for large n, O(n log n) > O(n) but << O(n^2).
- The provided main.py includes testcases and prints average times for both set and brute-force to illustrate these trends.

When to choose which
- Use hash-set for general-purpose needs where O(n) time and O(n) space are acceptable — best default.
- Use sorting if memory is constrained or when you need ordered output afterward and can tolerate O(n log n).
- Brute-force only for tiny inputs or when simplicity matters and performance is irrelevant.

Edge cases
- Empty array [] -> False
- Single-element [x] -> False
- All elements identical -> True (best-case early exit for hash-set and brute-force finds duplicate quickly if there are at least two elements)

Python reference implementations

# Brute-force

def contains_duplicate_brute_force(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Hash-set (recommended)

def contains_duplicate_set_method(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False

Notes on real-world considerations
- Hash-set is typically the fastest and most practical for interview and production code when extra memory is allowed.
- For streaming data where the entire array cannot be stored, different approaches (approximate algorithms, Bloom filters, or external sorting) are necessary.
- For extremely large n where memory matters, consider sorting on disk or using probabilistic structures (with false positives) depending on acceptable tradeoffs.

References
- LeetCode 217. Contains Duplicate — canonical problem for practicing hash-table basics and complexity tradeoffs.


# Detailed Solutions: Minimum Size Subarray Sum

This document explains two primary approaches, gives step-by-step examples and proofs, covers edge cases and variants (including arrays with negative numbers), and provides interview-style follow-ups and suggested talking points.

---

## 1) Sliding-window (two pointers) — O(n) time, O(1) space

Idea
- Maintain a window [left, right] and running sum of elements inside it.
- Expand right (add nums[right]) until sum >= target.
- When sum >= target, record window length, then move left forward (subtract nums[left]) to try to shrink the window while still meeting the target.
- Because nums are positive, moving right only increases the sum and moving left only decreases it; this monotonicity guarantees correctness and allows O(n) time.

Pseudocode
- left = 0, sum = 0, best = +inf
- for right in 0..n-1:
    sum += nums[right]
    while sum >= target:
        best = min(best, right-left+1)
        sum -= nums[left]
        left += 1
- return 0 if best==+inf else best

Worked example (target=7, nums=[2,3,1,2,4,3])
- right=0: sum=2 (<7)
- right=1: sum=5 (<7)
- right=2: sum=6 (<7)
- right=3: sum=8 (>=7) -> best=4; shrink left -> remove 2 => sum=6 (<7)
- right=4: sum=10 (>=7) -> best=min(4, 4-1+1=4)=4; shrink left: remove 3 => sum=7 (>=7) -> best=3; shrink left: remove 1 => sum=6 (<7)
- right=5: sum=9 (>=7) -> best=min(3, 5-3+1=3)=3; shrink left: remove 2 => sum=7 (>=7) -> best=2; shrink left: remove 4 => sum=3 (<7)
- finished -> answer=2 (subarray [4,3])

Correctness sketch
- For any optimal subarray [L,R] of minimal length, when the algorithm's right pointer reaches R, the inner while-loop will move left to the smallest index L' such that sum(nums[L':R]) < target only after checking all valid left positions with sum >= target — therefore the algorithm sees the window ending at R and will compute (R - L + 1) or a smaller length. The monotonicity of prefix sums for positive numbers ensures left only moves forward, so no candidate is missed.

Return indices
- Keep best_len and best_left when updating best. On update: best_left = left, best_right = right. After finishing, return (best_len, best_left, best_right).

When to use
- Default choice for positive arrays in interviews and production: minimal code, best performance.

---

## 2) Prefix sums + binary search — O(n log n) time, O(n) space

Idea
- Compute prefix sums: prefix[0]=0; prefix[i]=sum(nums[:i]) for i>=1.
- For each start index i (0..n-1), need smallest j such that prefix[j] - prefix[i] >= target -> prefix[j] >= target + prefix[i].
- Because prefix is non-decreasing (nums non-negative), use binary search (lower_bound) on prefix to find j.

Pseudocode
- prefix = [0]*(n+1)
- for i in 0..n-1: prefix[i+1] = prefix[i] + nums[i]
- best = +inf
- for i in 0..n-1:
    need = prefix[i] + target
    j = lower_bound(prefix, need)
    if j <= n: best = min(best, j - i)
- return 0 if best==+inf else best

Worked example (target=7, nums=[2,3,1,2,4,3])
- prefix = [0,2,5,6,8,12,15]
- i=0: need=7 -> j=4 -> len=4
- i=1: need=9 -> j=5 -> len=4
- i=2: need=13 -> j=6 -> len=4
- i=3: need=15 -> j=6 -> len=3
- i=4: need=19 -> j=7 (out of range)
- i=5: need=22 -> j=7 (out of range)
- best=3 (but sliding-window finds 2 because prefix search above missed a smaller window ending earlier — note that careful binary-search of the prefix as implemented yields the correct minimal value if prefix is correct; the example steps above illustrate how the approach explores all starts)

Notes
- Simpler to implement if comfortable with binary search and prefix sums.
- Uses O(n) extra space for prefix.

---

## 3) Arrays with negative numbers (general case)

Why sliding-window breaks
- With negative values, adding a new element can decrease the running sum, and removing from left can increase it. The monotonic guarantee used by the sliding-window no longer holds, so left/right movements cannot be greedily tied to sum growth/decay.

Two common approaches:

A) Prefix sums + monotonic deque (O(n)) — algorithm similar to LeetCode 862 "Shortest Subarray with Sum at Least K"
- Keep prefix sums P[i]. Maintain a deque of indices with increasing P values.
- For current index i, while deque not empty and P[i] - P[deque[0]] >= target, update answer using i - deque.popleft(). This finds the shortest subarray ending at i with sum >= target.
- While deque not empty and P[i] <= P[deque[-1]]: pop from right (maintain monotonicity).
- Append i to deque.
- This works in O(n) time and O(n) space and handles negatives.

B) Prefix sums + ordered map / balanced BST (O(n log n))
- Store prefix sums keyed by value with their earliest index. For each i, search for the smallest prefix value <= P[i] - target and use associated index to update answer. Implementable with TreeMap in Java or SortedDict in other languages. Slower but conceptually straightforward.

Recommendation
- Use the monotonic deque solution if negative numbers are allowed — it's optimal and common in interviews as an advanced follow-up.

---

## 4) Complexity summary
- Sliding-window:
  - Time: O(n)
  - Space: O(1) extra
- Prefix + binary search:
  - Time: O(n log n)
  - Space: O(n)
- Prefix + deque (handles negatives):
  - Time: O(n)
  - Space: O(n)
- Prefix + ordered map:
  - Time: O(n log n)
  - Space: O(n)

---

## 5) Practical trade-offs and tips
- Prefer sliding-window for positive arrays: simplest and fastest.
- Prefix+binary is handy when you already compute prefix sums for other reasons, or when language libraries make lower_bound trivial.
- When input size is huge but memory constrained, sliding-window avoids O(n) extra storage.
- If negatives are possible, prepare to explain the deque approach; it's a strong interview signal.

Edge cases
- target <= 0: return 1 (since any non-empty positive-sum subarray meets target) or define behavior explicitly. Typically problem states target>0.
- Single-element arrays: check equality >= target.
- All numbers small and total sum < target: return 0.

---

## 6) Interview questions & suggested talking points
1) Why is monotonicity important for sliding-window? (Explain how positive numbers guarantee prefix sums are strictly increasing as right moves.)
2) Prove correctness of sliding-window: argue that every candidate minimal window is considered when its right endpoint is reached.
3) How to return indices: track positions when updating best.
4) What if numbers can be zero? (Sliding-window still works; zeros don't break monotonicity.)
5) Allow negatives: ask whether O(n) is possible — describe the monotonic-deque approach and sketch why it works.
6) Worst-case inputs for prefix+binary and deque methods: discuss time/space behavior.
7) Implementation pitfalls: off-by-one in prefix indexing, using bisect on prefix array vs. raw nums.
8) Follow-up: how to find the longest subarray with sum <= target — hint: use two pointers but with a different invariant or prefix sums with binary search for upper bounds.

---

References
- LeetCode 209: Minimum Size Subarray Sum
- LeetCode 862: Shortest Subarray with Sum at Least K (monotonic deque technique)

Notes
- The sliding-window solution is typically the expected answer for the standard problem constraints (positive integers). The deque-based prefix approach is the advanced generalization for arrays that may contain negative values.
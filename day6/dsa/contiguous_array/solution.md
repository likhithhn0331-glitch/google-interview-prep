# Contiguous Array — Solutions and Interview Guide

Overview
--------
Given a binary array nums, find the maximum length of a contiguous subarray with equal numbers of 0s and 1s.

Two primary approaches are commonly discussed in interviews below: a brute-force (enumeration) approach and an optimal prefix-sum + hashmap approach. Both are explained, compared, and analyzed for time/space complexity. Interview-style follow-ups and hints are provided at the end.

Solution A — Brute-force (Enumerate subarrays)
----------------------------------------------
Idea
- Check every subarray, count zeros and ones (or compute difference) and track the longest that has equal counts.

Algorithm
1. For each start index i from 0..n-1:
   a. Maintain counters zeros=0 and ones=0 (or a delta variable).
   b. For end index j from i..n-1:
      - Update counters with nums[j].
      - If zeros == ones (or delta==0), update maxLen = max(maxLen, j-i+1).
2. Return maxLen.

Why it works
- It exhaustively examines every contiguous candidate; correctness is straightforward.

When to use
- Small inputs, or when implementing a quick correct solution before optimizing.

Downsides
- Quadratic time (and possibly cubic if naive counting inside nested loops), so it fails on large arrays (n up to 1e5).

Solution B — Prefix-sum with hashmap (optimal)
----------------------------------------------
Key observation
- Replace every 0 with -1. Then a subarray has equal numbers of 0s and 1s iff its sum is 0.
- Compute prefix sums; if the same prefix sum value appears at indices i and j (i<j), the subarray (i+1..j) sums to 0.

Algorithm (linear)
1. Initialize sum = 0, best = 0, and a map firstIdx that maps sum -> first index seen. Put firstIdx[0] = -1.
2. Iterate index i from 0..n-1:
   - If nums[i] == 0, sum += -1 else sum += 1.
   - If sum exists in firstIdx: candidateLen = i - firstIdx[sum]; best = max(best, candidateLen).
   - Else store firstIdx[sum] = i.
3. Return best.

Why it works
- When prefix sums repeat, the intermediate subarray sum is zero (equal number of -1 and +1 => equal 0s and 1s).
- Storing first occurrence ensures longest possible interval for that sum is considered.

When to use
- All practical inputs. This is the recommended interview solution.

Comparison
----------
- Time: Brute-force O(n^2) vs prefix-sum O(n).
- Space: Brute-force O(1) extra (if counting on the fly) vs prefix-sum O(n) for hashmap.
- Practical: Prefix-sum is vastly faster for large n; brute-force useful for conceptual correctness or tiny n.
- Simplicity: Brute-force is simpler to reason about; prefix-sum requires the 0->-1 trick and map usage.

Time & Space Complexity (detailed)
----------------------------------
Let n = nums.length.

Brute-force:
- Time: O(n^2) scanning all O(n^2) subarrays and updating counts in O(1) per extension. If counting from scratch per subarray, O(n^3) — avoid this by incrementally updating counts.
- Space: O(1) extra (only counters and loop indices).

Prefix-sum + hashmap:
- Time: O(n) — one pass through the array; hashmap operations average O(1).
- Space: O(n) — worst-case the prefix sums are all distinct and stored in the map (map size ≤ n+1).

Edge cases & notes
- All zeros or all ones -> result 0 (no equal split).
- Alternating patterns (e.g., [0,1,0,1]) -> full length if equal counts.
- Single element -> 0.
- The choice firstIdx[0] = -1 handles subarrays starting at index 0.
- Use an ordered map only if you need to inspect prefix order; a plain hash map suffices for correctness.

Variants and related problems
- Maximum-length subarray with sum equal to k (replace target behavior; same prefix-sum idea but check for sum-k in map).
- Longest subarray with equal letters or equal counts of two different values in a non-binary array (map differences between two counters).

Interview-style questions and follow-ups
---------------------------------------
1. Can you reduce the space complexity? (Trade-offs: hard to beat O(n) worst-case; for specific input distributions or streaming constraints consider two-pass techniques or compression.)
2. How would you adapt the solution for k different values (find longest subarray with equal counts for all k values)? (Use vectors of differences and hashing; complexity grows.)
3. What if input is a stream — can you do it online with bounded memory? (You can detect equal-length occurrences but not necessarily the global max without O(n) memory.)
4. How to modify to return the actual subarray indices (not just length)? (Store first index in map; when updating best, also record start = firstIdx[sum]+1 and end = i.)
5. What if 0 and 1 are not equally frequent overall — can the algorithm short-circuit? (No guaranteed short-circuit for worst-case; still must scan.)
6. Ask to prove correctness formally: show that repeated prefix sums imply subarray sum zero and conversely any zero-sum subarray causes repeated prefix sums.
7. Could there be hash collisions affecting correctness? (If using a correct hash map from language/library, it handles collisions — algorithmic correctness relies on equality of keys, not hash uniqueness.)

Implementation hints for interviews
- Start with the brute-force explanation to establish correctness, then present the O(n) optimization.
- Explain the 0 → -1 transformation explicitly and why firstIdx[0] = -1 is necessary.
- Mention complexity and edge cases before coding.

Small test cases to sanity check
- [] (if allowed) -> 0
- [0] -> 0
- [1] -> 0
- [0,1] -> 2
- [0,1,0] -> 2
- [0,0,1,1,0,1] -> 6 or appropriate longest length

Summary
-------
Brute-force is simple but inefficient. The prefix-sum + hashmap approach is the standard interview-grade solution: linear time, linear space, and easy to implement once the 0→-1 trick is described.


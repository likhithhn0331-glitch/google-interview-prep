# Daily Temperatures

## 1. Problem

Given an array `temperatures`, return `answer` where `answer[i]` is the number
of days after day `i` that must be waited to see a strictly warmer temperature.
If no warmer future day exists, `answer[i]` is `0`.

Example:

```text
Input:  [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

For example, day `2` has temperature `75`; the next warmer temperature is `76`
on day `6`, so `answer[2] = 6 - 2 = 4`.

## 2. Pattern

This is a **next greater element** problem using a **monotonic decreasing
stack**.

The stack stores indices of days that have not yet found a warmer future day.
Their temperatures are kept in decreasing order from the bottom toward the
top.

## 3. Recognition signal

Look for these phrases:

- "next warmer", "next greater", or "first larger value"
- the answer for each position depends on values to its right
- return the distance to the first qualifying future position
- input size is large enough that repeated forward scans are too expensive

When the answer for an earlier item can be completed as soon as a later item
arrives, a monotonic stack is usually a strong candidate.

## 4. Brute force

For every day `i`, scan all later days from left to right. The first day `j`
whose temperature is greater than `temperatures[i]` determines the answer.
If the scan reaches the end, leave the answer as `0`.

```text
answer = [0] * n
for i from 0 to n - 1:
    for j from i + 1 to n - 1:
        if temperatures[j] > temperatures[i]:
            answer[i] = j - i
            break
```

This approach is simple and is useful as a correctness oracle for testing the
optimized solution.

## 5. Why brute force is insufficient

In a decreasing or nearly decreasing input, each day may scan almost the entire
suffix before discovering that no warmer day exists. The number of comparisons
can be approximately:

```text
(n - 1) + (n - 2) + ... + 1 = O(n^2)
```

With `n = 100,000`, quadratic work is too slow and does not meet the intended
scalability of the problem.

## 6. Optimized idea

Process temperatures from left to right and keep unresolved day indices in a
monotonic decreasing stack.

When the current temperature is warmer than the temperature at the top index,
the current day is the first warmer day for that popped index. Set its answer
to the difference between the current index and the popped index. Continue
popping while the current temperature resolves more earlier days.

## 7. Invariant

Before processing the current day:

- every index in the stack has no warmer day among the days processed so far;
- indices in the stack are ordered from older to newer;
- temperatures at those indices are decreasing from bottom to top;
- every unresolved answer is still correctly initialized to `0`.

After all warmer stack entries are popped, pushing the current index restores
the decreasing-temperature order.

## 8. Algorithm

```text
answer = [0] * n
stack = []                         # indices, not temperatures

for i, temperature in enumerate(temperatures):
    while stack and temperature > temperatures[stack[-1]]:
        previous = stack.pop()
        answer[previous] = i - previous
    stack.append(i)

return answer
```

Use a strict `>` comparison because an equal temperature is not warmer.
Indices are stored so that the waiting distance can be calculated directly.
Any indices left in the stack have no warmer day to their right, so their
answers correctly remain `0`.

## 9. Dry run

For `[73, 74, 75, 71, 69, 72, 76, 73]`:

| Index | Temperature | Action | Stack (indices) | Answer |
|---:|---:|---|---|---|
| 0 | 73 | Push 0 | `[0]` | `[0,0,0,0,0,0,0,0]` |
| 1 | 74 | Pop 0; `1 - 0 = 1`; push 1 | `[1]` | `[1,0,0,0,0,0,0,0]` |
| 2 | 75 | Pop 1; `2 - 1 = 1`; push 2 | `[2]` | `[1,1,0,0,0,0,0,0]` |
| 3 | 71 | Push 3 | `[2,3]` | `[1,1,0,0,0,0,0,0]` |
| 4 | 69 | Push 4 | `[2,3,4]` | `[1,1,0,0,0,0,0,0]` |
| 5 | 72 | Pop 4; `5 - 4 = 1`; pop 3; `5 - 3 = 2`; push 5 | `[2,5]` | `[1,1,0,2,1,0,0,0]` |
| 6 | 76 | Pop 5; `6 - 5 = 1`; pop 2; `6 - 2 = 4`; push 6 | `[6]` | `[1,1,4,2,1,1,0,0]` |
| 7 | 73 | Push 7 | `[6,7]` | `[1,1,4,2,1,1,0,0]` |

The remaining indices `6` and `7` are unresolved, so their values stay `0`.

## 10. Complexity

### Brute force

- Time: `O(n^2)` worst case
- Extra space: `O(1)`, excluding the output array
- Output space: `O(n)`

### Monotonic stack

- Time: `O(n)`: every index is pushed once and popped at most once
- Extra space: `O(n)` for the stack and output array

## 11. Edge cases

- One temperature: `[70] -> [0]`
- Strictly decreasing values: every result is `0`
- Strictly increasing values: every result except the last is `1`
- All equal values: every result is `0`
- The warmer day is far away
- The warmer day is immediately next
- Negative or non-standard integer values, if the input contract allows them
- Empty input, if the implementation is expected to support it

## 12. Common mistakes

- Storing temperatures instead of indices, which loses the waiting distance.
- Using `>=` instead of `>`, incorrectly treating equal temperatures as warmer.
- Popping only one item instead of continuing until the stack is valid.
- Scanning from the wrong direction without changing the algorithm accordingly.
- Assigning an answer to the current index instead of the popped index.
- Forgetting that unresolved stack entries should remain `0`.
- Claiming the stack algorithm is quadratic because of the nested-looking
  `while`; each index can be popped only once, so the total is linear.

## 13. Alternative approach

A right-to-left dynamic-programming variant can jump over days that are not
warmer:

1. For each day, start at the next day.
2. If that day is not warmer and already has a known answer, jump ahead by that
   answer.
3. Continue until a warmer day is found or the end is reached.

This can be efficient for bounded temperature ranges, but it is more subtle
than the monotonic stack and the stack solution is the clearest general
approach.

## 14. Interview follow-ups

### Why does the stack contain indices rather than values?

The result is a number of days, so the algorithm needs both the current index
and the unresolved day's index. The temperature can always be retrieved from
the original array.

### Why is the total stack work `O(n)` despite the `while` loop?

Every index is pushed exactly once. Once an index is popped, it is removed
permanently and cannot be pushed again. Therefore, across the entire loop,
there are at most `n` pushes and `n` pops.

### Why are equal temperatures not popped?

The requirement is a *strictly warmer* future day. If the current temperature
equals the stack temperature, it does not resolve that earlier day, so the
earlier index remains in the stack.

### What does a remaining stack entry mean after the scan?

It means no later temperature is strictly warmer than that day's temperature.
Its initialized answer of `0` is therefore correct.

### Can the stack store `(temperature, index)` pairs?

Yes. Storing pairs avoids indexing back into the input array, but storing only
indices is usually simpler and avoids duplicating temperature data.

### How would you return the next warmer temperature instead of the distance?

When popping an index, store `temperatures[i]` rather than `i - previous`.
The same monotonic-stack invariant applies.

### How would you find the next warmer day in a circular array?

Process up to `2 * n` positions and use `i % n` for the temperature index.
Only the first `n` positions should receive answers, and indices must be
handled so that a day does not match itself.

### What if the question asks for the next greater-or-equal temperature?

Change the comparison rule deliberately. Equal values would then resolve an
entry, so the pop condition would be `current >= temperatures[stack[-1]]`.


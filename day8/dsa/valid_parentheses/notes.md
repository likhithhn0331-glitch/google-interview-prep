# Valid Parentheses - Interview Notes

## Problem

Given a string containing only `()`, `[]`, and `{}`, determine whether every
opening bracket has a matching closing bracket and whether brackets close in
the correct order.

A string is valid when:

1. Each opening bracket has exactly one closing bracket of the same type.
2. Brackets are closed in last-in, first-out order.
3. No closing bracket appears without its corresponding opening bracket.

Examples:

- `"{[]}"` is valid.
- `"([)]"` is invalid because `)` tries to close `[` first.
- `"((("` is invalid because the openings are never closed.
- `""` is valid because there are no unmatched brackets.

## Pattern

This is a delimiter-matching problem using the **stack** pattern. It is also a
classic example of recognizing last-in, first-out behavior in a string.

## Recognition signal

Think of a stack when:

- items must be matched in reverse order of arrival;
- the most recently opened group must be closed first;
- nested structures such as brackets, tags, or function calls are involved;
- a single left-to-right scan should be possible.

The phrase "correct order" is the strongest signal: it means the latest
unmatched opening bracket is the only bracket that the next closing bracket can
close.

## Brute force

The brute-force implementation repeatedly removes adjacent valid pairs:
`"()"`, `"[]"`, and `"{}"`.

For example:

```text
"{[()]}" -> "{[]}" -> "{}" -> ""
```

After each pass:

1. Replace every known adjacent pair with an empty string.
2. If the string did not change and characters remain, return `False`.
3. If all characters are removed, return `True`.

This method is implemented in `brute_force.py`.

## Why brute force is insufficient

Removing pairs requires rebuilding the string. A deeply nested input may remove
only one layer per pass, so the algorithm can perform `O(n)` passes, each
touching `O(n)` characters. Its worst-case time complexity is therefore
`O(n^2)`.

It is useful as a simple reference implementation and as an independent
comparison oracle, but it is not the preferred production solution for inputs
near the maximum length.

## Optimized idea

Scan once with a stack:

- Push opening brackets.
- For a closing bracket, compare it with the stack top.
- Pop only when the types match.
- Reject immediately when the stack is empty or the types differ.

The stack contains exactly the opening brackets that have been seen but not
closed yet.

## Invariant

After processing any prefix of the input:

- the stack contains all unmatched opening brackets from that prefix;
- they are stored in their opening order;
- the top of the stack is the only opening bracket that the next closing
  bracket is allowed to match.

If a closing bracket does not match the top, no later input can repair that
ordering error, so returning `False` immediately is safe.

## Algorithm

1. Initialize an empty stack.
2. For each character:
   - If it is an opening bracket, push it.
   - Otherwise, look up its expected opening bracket.
   - If the stack is empty or its top is not the expected opening bracket,
     return `False`.
   - Pop the matching opening bracket.
3. Return `True` only when the stack is empty.

`stacks.py` uses a set for opening brackets and a mapping from each closing
bracket to its matching opening bracket.

## Dry run

Input: `"{[()]}"`.

| Character | Action | Stack |
|---|---|---|
| `{` | push | `{` |
| `[` | push | `{ [` |
| `(` | push | `{ [ (` |
| `)` | matches `(`, pop | `{ [` |
| `]` | matches `[`, pop | `{` |
| `}` | matches `{`, pop | empty |

The final stack is empty, so the input is valid.

Input: `"([)]"`.

| Character | Action | Stack |
|---|---|---|
| `(` | push | `(` |
| `[` | push | `( [` |
| `)` | expected `(`, but top is `[` | reject |

The string is invalid even though the counts of opening and closing brackets
are equal.

## Complexity

Let `n` be the string length.

| Approach | Time | Extra space |
|---|---:|---:|
| Repeated pair removal | `O(n^2)` worst case | `O(n)` |
| Stack scan | `O(n)` | `O(n)` |

The stack solution processes each character once. The stack can contain all
`n` characters for an input made entirely of opening brackets.

## Edge cases

- Empty string: valid.
- One opening bracket such as `"("`: invalid.
- One closing bracket such as `")"`: invalid.
- Mismatched pair such as `"(]"`: invalid.
- Wrong nesting such as `"([)]"`: invalid.
- Consecutive independent pairs such as `"()[]{}"`: valid.
- Fully nested brackets such as `"{[()]}"`: valid.
- A long sequence of opening brackets: tests maximum stack growth.
- A closing bracket encountered early: should return `False` immediately.

## Common mistakes

- Checking only whether opening and closing counts are equal; this misses
  ordering errors such as `"([)]"`.
- Popping before checking the stack top.
- Comparing a closing bracket with the wrong opening bracket.
- Forgetting to reject a closing bracket when the stack is empty.
- Returning `True` without checking for leftover opening brackets.
- Using a counter instead of a stack when multiple bracket types are present.
- Assuming the last character being a closing bracket is sufficient.

## Alternative approach

The repeated-removal method in `brute_force.py` is the direct alternative.
Another implementation of the optimized approach can push the expected closing
bracket instead of the opening bracket. On an opening bracket, it pushes its
expected closer; on a closing bracket, it checks whether it equals the stack
top.

The expected-closer variant can make the comparison especially concise, but
both versions have the same `O(n)` time and `O(n)` space complexity.

## Interview follow-ups

### Why is a stack the correct data structure?

Nested brackets require last-in, first-out matching. The most recently opened
bracket must be the first one closed, which is exactly stack behavior.

### Can the solution use `O(1)` extra space?

Not for arbitrary nesting with multiple bracket types. The algorithm must
remember the sequence of unmatched opening bracket types, which can require
`O(n)` space. With only one bracket type, a counter would be enough.

### How would you support additional delimiter types?

Add the new opening delimiter to the opening set and add its closing delimiter
and matching opening delimiter to the mapping. The scan itself does not
change.

### Why can the algorithm stop at the first mismatch?

A mismatch means the current closing bracket cannot match the most recent
unmatched opening bracket. Since bracket order is fixed, later characters
cannot change that already-invalid prefix.

### What changes if non-bracket characters are allowed?

Ignore characters that are not delimiters, unless the problem defines another
meaning for them. The matching logic remains unchanged.

### How would you test the implementations?

Use valid pairs, nested pairs, independent pairs, mismatches, wrong nesting,
unclosed openings, premature closings, the empty string, and long inputs.
`main.py` runs shared cases through both implementations and checks their
results against expected answers.

### How would you explain correctness?

The invariant says the stack contains exactly the unmatched openings for the
processed prefix. A matching close removes the most recent opening and
preserves the invariant. A mismatch proves the prefix invalid. At the end, an
empty stack means every opening was matched; a non-empty stack means at least
one opening was not closed.

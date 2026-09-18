# Valid Parentheses

## Problem

Given a string containing only `()`, `[]`, and `{}`, determine whether every
opening bracket has a matching closing bracket and whether brackets close in
the correct order.

For example, `"{[]}"` is valid because each pair is correctly nested, while
`"([)]"` is invalid because the brackets close in the wrong order.

The empty string is also considered valid: it contains no unmatched brackets.

## Brute-force solution

The innermost valid pairs in a well-formed string are adjacent. Repeatedly
remove every occurrence of `()`, `[]`, and `{}` from the string. If the string
becomes empty, it was valid. If a complete pass makes no progress while
characters remain, an unmatched or incorrectly ordered bracket exists.

```python
while s:
    remove all (), [], and {}
    if nothing was removed:
        return False
return True
```

Creating a new string during each pass costs `O(n)` time. In the worst case,
only one pair is removed per pass, so there can be `O(n)` passes.

- **Time complexity:** `O(n^2)`
- **Space complexity:** `O(n)`

The `O(n)` space accounts for the new strings created while reducing the
input. The input string itself is not modified.

## Stack solution

Scan the string from left to right:

1. Push every opening bracket onto a stack.
2. For a closing bracket, return `False` if the stack is empty.
3. Otherwise, compare it with the opening bracket on top of the stack.
4. Return `False` if the types do not match; otherwise, pop the opening
   bracket.
5. After the scan, the string is valid only if the stack is empty.

The stack stores unmatched opening brackets, which guarantees that the most
recent opening bracket is closed first.

- **Time complexity:** `O(n)`
- **Space complexity:** `O(n)`

## Possible interview questions

### 1. Why is a stack the right data structure?

Brackets must be closed in the reverse order in which they are opened. This is
last-in, first-out behavior, which is exactly what a stack provides.

### 2. Why is `"([)]"` invalid?

After reading `"(["`, the most recent opening bracket is `"["`. The next
character is `")"`, which does not match `"["`, so the string is invalid.

### 3. What happens if a closing bracket appears first?

The stack is empty, so there is no opening bracket to match it. The algorithm
returns `False` immediately. For example, `")("` is invalid.

### 4. Why must the stack be empty at the end?

An empty stack means every opening bracket found a matching closing bracket. If
openings remain in the stack, the string contains unclosed brackets, such as
`"(( "` or `"["`.

### 5. What is the maximum stack size?

`O(n)`, reached when the input consists entirely of opening brackets, such as
`"(((([["`.

### 6. Can the algorithm stop early?

Yes. It can return `False` as soon as it finds a closing bracket with no
matching opening bracket or a closing bracket of the wrong type. This does not
change the worst-case complexity.

### 7. What is the difference between the two solutions?

The brute-force solution repeatedly creates reduced strings and can take
`O(n^2)` time. The stack solution processes each character once and takes
`O(n)` time, so it is the preferred production and interview solution.

### 8. How would you support additional bracket types?

Add each opening bracket to the set of opening brackets and add its closing
bracket and corresponding opening bracket to the mapping. The algorithm
otherwise remains unchanged.

### 9. Is the empty string valid?

Yes. It contains no unmatched brackets, so the final stack is empty. The
provided implementation returns `True` for it.

### 10. Can this be solved with constant extra space?

For arbitrary nesting depth, not in the general case. The algorithm must retain
the unmatched opening brackets, which may require `O(n)` space. If the input
contained only one bracket type, a counter would be sufficient, but multiple
types require preserving their order.

## Running the tests

Run the comparison test script from this directory:

```text
python main.py
```

`main.py` runs the same test cases through both implementations, checks their
expected results, and verifies that their outputs agree.

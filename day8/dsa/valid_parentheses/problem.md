# Valid Parentheses

## Problem Statement

Given a string `s` containing only the characters

- `'('`
- `')'`
- `'{'`
- `'}'`
- `'['`
- `']'`

Determine whether the input string is valid.

A string is considered valid if

1. Every opening bracket has a corresponding closing bracket of the same type.
2. Opening brackets are closed in the correct order.
3. Every closing bracket has a matching opening bracket before it.

Return `true` if the string is valid, otherwise return `false`.

---

## Examples

### Example 1

Input
```text
s = ()
```

Output
```text
true
```

### Example 2

Input
```text
s = ()[]{}
```

Output
```text
true
```

### Example 3

Input
```text
s = (]
```

Output
```text
false
```

### Example 4

Input
```text
s = ([)]
```

Output
```text
false
```

### Example 5

Input
```text
s = {[]}
```

Output
```text
true
```

---

## Constraints

- `1 = s.length = 10^4`
- `s` consists only of parentheses characters `'()[]{}'`.

---

## Approach Hint

Use a stack data structure

1. Push every opening bracket onto the stack.
2. When a closing bracket is encountered
   - Check if the stack is empty.
   - Verify that the top element matches the corresponding opening bracket.
3. Pop the matched opening bracket.
4. After processing the entire string
   - If the stack is empty, the string is valid.
   - Otherwise, it is invalid.

---

## Complexity Analysis

- Time Complexity `O(n)`
- Space Complexity `O(n)`

where `n` is the length of the string.

---

## Tags

`Stack` `String` `Data Structures`
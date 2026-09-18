---

## Constraints

- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator (`"+"`, `"-"`, `"*"`, `"/"`) or an integer in the range `[-200, 200]`.
- The input represents a valid Reverse Polish Notation expression.
- The result and all intermediate calculations fit in a 32-bit signed integer.

---

## Approach Hint

Use a stack:

1. Traverse each token from left to right.
2. If the token is a number, push it onto the stack.
3. If the token is an operator:
   - Pop the top two elements from the stack.
   - Apply the operator.
   - Push the result back onto the stack.
4. After processing all tokens, the stack will contain exactly one element, which is the answer.

---

## Complexity Analysis

### Stack Solution

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

where `n` is the number of tokens.

---

## Tags

`Array` `Stack` `Math`
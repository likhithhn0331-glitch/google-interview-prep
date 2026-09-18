# Evaluate Reverse Polish Notation

## 1. Problem

Given a valid reverse Polish notation (RPN) expression, evaluate it and return the result.

Example:
- Input: ["2", "1", "+", "3", "*"]
- Output: 9
- Explanation: ((2 + 1) * 3) = 9

Each token is either:
- an integer value, or
- one of the operators: `+`, `-`, `*`, `/`

The expression is guaranteed to be valid.

## 2. Pattern

This problem follows the Stack + Postfix Expression pattern.

Recognition signals:
- Operators appear after operands.
- The expression is in postfix form.
- The result depends on evaluating the most recent operands.
- The problem asks to process tokens left to right with nested operations.

This is a classic stack problem because postfix notation naturally pairs operators with the two most recently seen values.

## 3. Recognition signal

You should immediately think of a stack when you see:
- expressions like `a b +` or `2 3 + 4 *`
- postfix notation
- evaluation where operators act on recent operands
- need for efficient single-pass processing

The key is: in RPN, every operator consumes the last two values currently available.

## 4. Brute force

A brute-force idea is to repeatedly scan the token list and reduce the expression.

Example:
- ["2", "1", "+", "3", "*"]
- Find `+` and replace `2 1 +` with `3`
- Expression becomes ["3", "3", "*"]
- Compute `3 * 3 = 9`

Pseudo-code:

```
while len(tokens) > 1:
    find the first operator in the current expression
    evaluate the two values before it
    replace the three-part pattern with the result
```

This directly follows the definition of postfix evaluation but is not efficient.

## 5. Why brute force is insufficient

The brute-force method repeatedly scans the list to find the next operator and rebuilds the expression.

This causes repeated work across the remaining tokens.

In the worst case:
- each pass may scan a large portion of the expression
- reducing and rewriting tokens adds extra overhead
- overall time becomes O(n^2)

When input length can be up to 10^4, this is too slow for an interview-quality optimal solution.

## 6. Optimized idea

Use a stack.

Algorithm:
- Traverse the tokens from left to right.
- If token is a number, push it onto the stack.
- If token is an operator, pop the last two values.
- Apply the operator to them.
- Push the result back.
- At the end, only one value remains on the stack.

This is the standard optimal solution for RPN evaluation.

## 7. Invariant

At every step of processing tokens:

- the stack contains the results of fully evaluated subexpressions
- any pending operand sequence is represented on the stack in correct order
- the next operator will consume the top two values exactly as required by postfix notation

This invariant guarantees correctness as the scan continues.

## 8. Algorithm

```
stack = []

for token in tokens:
    if token is a number:
        stack.push(int(token))
    else:
        if stack has fewer than 2 elements:
            invalid expression
        right = stack.pop()
        left = stack.pop()
        result = evaluate(left, right, token)
        stack.push(result)

return stack[0]
```

### Operator evaluation

```
if token == '+': return left + right
if token == '-': return left - right
if token == '*': return left * right
if token == '/': return truncation_toward_zero(left / right)
```

Important note for division:
- In Python, `//` floors toward negative infinity
- But RPN problem statements usually expect truncation toward zero
- So division logic should handle the sign carefully

## 9. Dry run

Take input:
`["4", "13", "5", "/", "+"]`

Step-by-step:

1. token = "4" -> stack = [4]
2. token = "13" -> stack = [4, 13]
3. token = "5" -> stack = [4, 13, 5]
4. token = "/" -> pop 5 and 13
   - compute 13 / 5 = 2 (trunc toward zero)
   - push 2 -> stack = [4, 2]
5. token = "+" -> pop 2 and 4
   - compute 4 + 2 = 6
   - push 6 -> stack = [6]

Final answer: `6`

Another example:
`["2", "1", "+", "3", "*"]`

1. push 2 -> [2]
2. push 1 -> [2, 1]
3. "+" -> pop 1, 2 => 3 -> [3]
4. push 3 -> [3, 3]
5. "*" -> pop 3, 3 => 9 -> [9]

Answer: `9`

## 10. Complexity

### Brute force
- Time: O(n^2)
- Space: O(n)

Reason: repeated scanning and expression reduction.

### Stack solution
- Time: O(n)
- Space: O(n)

Reason: each token is processed once; stack holds intermediate results.

## 11. Edge cases

- Single-element expression: `["5"]`
- Multiple nested operations: `["1", "2", "+", "3", "*", "4", "+"]`
- Negative numbers: `["-2", "-3", "*"]`
- Division with negative values: `["7", "-3", "/"]` => `-2`
- Expression with many tokens: large input up to 10^4
- Invalid tokens or malformed expression

## 12. Common mistakes

- Using the wrong order when popping operands
  - For `a b +`, correct is `left = a`, `right = b`
  - If you pop in the wrong order, answers become incorrect
- Using Python `//` directly for division
  - It floors negatively, which may not match problem expectations
- Forgetting to validate stack size before applying an operator
- Not checking that exactly one value remains at the end
- Confusing infix and postfix notation

## 13. Alternative approach

A brute-force reduction approach is the main alternative.

It works by repeatedly reducing the expression:
- locate an operator
- evaluate the preceding two operands
- replace the expression fragment with the result

This is conceptually simple but inefficient.

The stack is the preferred alternative because it processes each token in constant time and is ideal for postfix evaluation.

## 14. Interview follow-ups

### Follow-up 1: Why not use recursion?

Recursion can solve the problem by evaluating postfix recursively, but it is less natural and less efficient than the stack. The stack is simpler and more elegant for iterative token processing.

### Follow-up 2: What if the expression contains invalid input?

You should guard against malformed expressions by checking:
- not enough operands before an operator
- too many remaining values after processing
- unsupported operators

### Follow-up 3: How do you handle division semantics?

Use truncation toward zero rather than floor division when required by the problem. This is important because integer division in Python differs from typical interview expectations for negative numbers.

### Follow-up 4: Can this expression be evaluated in-place?

Not efficiently in a typical array-based solution. A stack is preferred because the data structure naturally supports last-in-first-out evaluation. In-place editing without a stack becomes more complex and less clean.

### Follow-up 5: What if we had to evaluate infix notation instead?

Then we would need precedence parsing, parenthesis handling, and possibly a shunting-yard algorithm or expression tree. Postfix notation is easier to evaluate because the operators already appear in the correct order.

## 15. Final takeaway

The problem is solved most cleanly with a stack because postfix notation guarantees that the next operator always acts on the two most recent computed values.

This leads to:
- Time complexity: O(n)
- Space complexity: O(n)

This is the standard optimal solution and the one usually expected in interviews.

# Evaluate Reverse Polish Notation

Given a valid Reverse Polish Notation (RPN) expression, evaluate it and return the result.

Example:
- Input: ["2", "1", "+", "3", "*"]
- Output: 9
- Explanation: ((2 + 1) * 3) = 9

Reverse Polish Notation is a postfix expression where operators come after their operands. This makes evaluation straightforward because the order of operations is naturally encoded in the token sequence.

## Problem Statement

You are given an array of strings `tokens` representing a valid RPN expression.

Each token is either:
- an integer value, or
- one of the operators: `+`, `-`, `*`, `/`

The expression is guaranteed to be valid and to produce an integer result.

Your task is to compute the numeric value of the expression.

## Key Observation

In postfix notation, whenever an operator is encountered, the previous two values are its operands.

For example:
- `2 1 +` means `2 + 1`
- `2 1 + 3 *` means `(2 + 1) * 3`

This is the reason a stack is so effective: the stack naturally stores values until an operator is ready to consume them.

## Brute-Force Solution

### Idea

Repeatedly scan the token list for an operator. When you find one, evaluate the two values immediately before it, replace those three tokens with the result, and continue until only one value remains.

### Example

Tokens: ["2", "1", "+", "3", "*"]

- Find `+` at index 2
- Evaluate `2 + 1 = 3`
- Replace `[2, 1, +]` with `[3]`
- Expression becomes `[3, 3, *]`
- Find `*`
- Evaluate `3 * 3 = 9`
- Final result: `9`

### Why it works

This approach directly follows the meaning of postfix notation. Every time an operator appears, the expression is reduced to a simpler equivalent expression. Repeating this until no operators remain gives the final answer.

### Complexity

- Time complexity: O(n^2)
- Space complexity: O(n)

Why quadratic? The algorithm restarts scanning after each reduction, so in the worst case each pass may examine many remaining tokens.

## Stack Solution

### Idea

Traverse the tokens from left to right.

- If the token is a number, push it onto the stack.
- If the token is an operator, pop the top two values, apply the operator, and push the result back.

At the end, exactly one value remains on the stack, which is the result.

### Example Walkthrough

Input: ["4", "13", "5", "/", "+"]

Process tokens one by one:
- push `4` -> [4]
- push `13` -> [4, 13]
- push `5` -> [4, 13, 5]
- `/` -> pop `5` and `13`, compute `13 / 5` -> 2, push `2` -> [4, 2]
- `+` -> pop `2` and `4`, compute `4 + 2` -> 6, push `6` -> [6]

Final result: `6`

### Why it works

In postfix notation, the stack preserves the correct operand order. The most recent two values are always the operands for the next operator. The stack automatically handles nested operations exactly as needed.

### Complexity

- Time complexity: O(n)
- Space complexity: O(n)

Each token is processed once, and the stack can hold at most one value per token in the worst case.

## Comparison

| Method | Time | Space | Readability | Best Use |
|---|---:|---:|---|---|
| Brute-force reduction | O(n^2) | O(n) | Easy to understand | Teaching, small inputs |
| Stack-based | O(n) | O(n) | Elegant and efficient | Production, interviews |

The stack method is the standard optimal solution and is the one usually expected in algorithm interviews.

## Interview Questions and Answers

### 1. What is Reverse Polish Notation?

Answer:

Reverse Polish Notation is postfix notation, which means operators appear after their operands. For example, `a b +` corresponds to `a + b`, while `a b c * +` corresponds to `a + (b * c)`.

This notation removes the need for parentheses and precedence rules during evaluation, because the order is embedded in the token sequence.

### 2. Why is a stack the natural data structure for this problem?

Answer:

A stack is ideal because it follows the Last-In-First-Out (LIFO) rule. In postfix expressions, when an operator is found, it uses the two most recently computed values. The stack ensures those values are available immediately and in the correct order.

This makes the evaluation both simple and efficient: numbers are pushed as they appear, and operators consume the relevant values from the top of the stack.

### 3. How do you handle division in RPN evaluation?

Answer:

Division must follow the requirement of the problem, which is typically truncation toward zero instead of floor division. In Python, plain `//` floors toward negative infinity, which is not the same as truncating toward zero.

To match standard integer division semantics, the implementation should compute:

- absolute values,
- divide them,
- restore the sign.

Example:
- `-7 / 3` should be `-2`, not `-3`
- `7 / -3` should be `-2`

This is often an important interview detail because many candidates forget the sign handling when using Python's `//` operator.

### 4. Why is the brute-force method slower than the stack method?

Answer:

The brute-force method repeatedly scans the array to find an operator, evaluates it, and rebuilds the expression. Each reduction may force another full pass over the remaining tokens. In the worst case, this makes the total time proportional to O(n^2).

By contrast, the stack method processes each token exactly once, so it has linear time complexity.

### 5. What happens if the expression is invalid?

Answer:

A valid RPN expression ensures that an operator is only applied when at least two numbers are available on the stack. If the input is malformed, the algorithm should raise an error or return a clear failure state.

In a production or interview setting, you might also validate:
- not enough operands before an operator,
- too many values left at the end,
- unsupported operator tokens.

This guards against accidental misuse and makes the logic robust.

### 6. Can this be solved without stacks?

Answer:

Yes, a brute-force reduction approach can work, but it is less efficient. It repeatedly reduces the expression by searching for operators and replacing them with results.

However, because postfix expressions are naturally stack-friendly, the stack approach is the right solution for both time efficiency and conceptual clarity.

### 7. What is the advantage of postfix expressions in compiler design?

Answer:

Postfix expressions eliminate ambiguity and remove the need to parse precedence and parentheses while evaluating. They are especially useful in expression evaluators, stack machines, and compiler intermediate representations.

This is one reason RPN is a classic interview problem: it tests understanding of both postfix notation and the stack data structure.

## Summary

The most efficient solution is to use a stack while scanning from left to right:

- numbers are pushed,
- operators pop two values,
- the result is pushed back,
- the single remaining value is the answer.

This gives:
- Time: O(n)
- Space: O(n)

It is the standard optimal approach for evaluating valid Reverse Polish Notation expressions.

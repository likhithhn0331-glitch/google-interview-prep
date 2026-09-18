"""Stack-based solution for evaluating reverse Polish notation."""

from typing import List


def apply_operator(left: int, right: int, operator: str) -> int:
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        quotient = abs(left) // abs(right)
        if (left < 0) ^ (right < 0):
            quotient = -quotient
        return quotient
    raise ValueError(f"Unsupported operator: {operator}")


def evaluate_rpn_stack(tokens: List[str]) -> int:
    """Use a stack to evaluate postfix expressions in O(n) time."""
    stack: List[int] = []

    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            if len(stack) < 2:
                raise ValueError("Invalid reverse Polish notation expression")

            right = stack.pop()
            left = stack.pop()
            result = apply_operator(left, right, token)
            stack.append(result)
        else:
            stack.append(int(token))

    if len(stack) != 1:
        raise ValueError("Invalid reverse Polish notation expression")

    return stack[0]


if __name__ == "__main__":
    sample = ["4", "13", "5", "/", "+"]
    print(evaluate_rpn_stack(sample))

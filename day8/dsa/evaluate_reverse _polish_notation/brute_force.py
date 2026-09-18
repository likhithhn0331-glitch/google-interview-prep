"""Brute-force solution for evaluating reverse Polish notation."""

from typing import List, Union


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


def evaluate_rpn_bruteforce(tokens: List[str]) -> int:
    """A simple brute-force reduction approach.

    The algorithm repeatedly scans the expression for an operator, evaluates the
    previous two numbers, replaces the triple with the result, and continues until
    only a single value remains.
    """
    expression = [str(token) for token in tokens]

    while len(expression) > 1:
        reduced = False

        for i in range(2, len(expression)):
            if expression[i] not in {"+", "-", "*", "/"}:
                continue

            left = int(expression[i - 2])
            right = int(expression[i - 1])
            result = apply_operator(left, right, expression[i])
            expression = expression[: i - 2] + [str(result)] + expression[i + 1 :]
            reduced = True
            break

        if not reduced:
            raise ValueError("Invalid reverse Polish notation expression")

    return int(expression[0])


if __name__ == "__main__":
    sample = ["2", "1", "+", "3", "*"]
    print(evaluate_rpn_bruteforce(sample))

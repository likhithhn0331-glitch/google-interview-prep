"""Stack-based solution for the valid parentheses problem."""


def is_valid(s: str) -> bool:
    """Return whether every bracket is closed in the correct order."""
    opening_brackets = {"(", "[", "{"}
    closing_to_opening = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []

    for bracket in s:
        if bracket in opening_brackets:
            stack.append(bracket)
        else:
            if not stack or stack[-1] != closing_to_opening.get(bracket):
                return False
            stack.pop()

    return not stack

"""Brute-force solution for the valid parentheses problem."""


def is_valid(s: str) -> bool:
    """Return whether all brackets can be removed in matching adjacent pairs."""
    matching_pairs = ("()", "[]", "{}")

    while s:
        reduced = s
        for pair in matching_pairs:
            reduced = reduced.replace(pair, "")

        if reduced == s:
            return False
        s = reduced

    return True

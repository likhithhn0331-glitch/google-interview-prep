from brute_force import is_valid as brute_force_is_valid
from stacks import is_valid as stack_is_valid


TEST_CASES = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("(((", False),
    ("))", False),
    ("", True),
    ("{[()]}", True),
    ("([{}])[]{}", True),
]


def run_tests() -> None:
    """Run the same test cases against both implementations."""
    for expression, expected in TEST_CASES:
        brute_force_result = brute_force_is_valid(expression)
        stack_result = stack_is_valid(expression)

        assert brute_force_result == expected, (
            f"Brute-force solution failed for {expression!r}: "
            f"expected {expected}, got {brute_force_result}"
        )
        assert stack_result == expected, (
            f"Stack solution failed for {expression!r}: "
            f"expected {expected}, got {stack_result}"
        )
        assert brute_force_result == stack_result

        print(
            f"{expression!r:12} expected={expected!s:5} "
            f"brute_force={brute_force_result!s:5} stack={stack_result!s:5}"
        )

    print(f"\nAll {len(TEST_CASES)} test cases passed.")


if __name__ == "__main__":
    run_tests()
from brute_force import evaluate_rpn_bruteforce
from stacks import evaluate_rpn_stack


def run_test_case(tokens, expected):
    brute_force_result = evaluate_rpn_bruteforce(tokens)
    stack_result = evaluate_rpn_stack(tokens)

    print(f"Tokens: {tokens}")
    print(f"Brute force: {brute_force_result}")
    print(f"Stack: {stack_result}")
    print(f"Expected: {expected}")

    assert brute_force_result == expected, (
        f"Brute force mismatch: expected {expected}, got {brute_force_result}"
    )
    assert stack_result == expected, (
        f"Stack mismatch: expected {expected}, got {stack_result}"
    )
    assert brute_force_result == stack_result, (
        f"Outputs differ: brute_force={brute_force_result}, stack={stack_result}"
    )
    print("PASS")
    print("-" * 40)


if __name__ == "__main__":
    test_cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
        (["3", "4", "+", "2", "*"], 14),
        (["-2", "-3", "*"], 6),
        (["7", "-3", "/"], -2),
        (["1", "2", "+", "3", "+"], 6),
    ]

    for tokens, expected in test_cases:
        run_test_case(tokens, expected)

    print("All test cases passed.")

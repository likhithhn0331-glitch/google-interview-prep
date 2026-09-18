from brute_force import daily_temperatures_bruteforce
from stacks import daily_temperatures_stack


def run_tests():
    test_cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([1, 2, 3, 4], [1, 1, 1, 0]),
        ([5, 4, 3, 2, 1], [0, 0, 0, 0, 0]),
        ([30, 10, 20, 40], [3, 1, 1, 0]),
        ([7, 7, 7, 7], [0, 0, 0, 0]),
    ]

    for index, (temperatures, expected) in enumerate(test_cases, start=1):
        brute_force_result = daily_temperatures_bruteforce(temperatures)
        stack_result = daily_temperatures_stack(temperatures)

        print(f"Test case {index}:")
        print(f"  Input:      {temperatures}")
        print(f"  Expected:   {expected}")
        print(f"  Brute force: {brute_force_result}")
        print(f"  Stack:      {stack_result}")

        assert brute_force_result == expected, (
            f"Brute force failed for case {index}: {brute_force_result} != {expected}"
        )
        assert stack_result == expected, (
            f"Stack solution failed for case {index}: {stack_result} != {expected}"
        )

        print("  Status: PASS")

    print("\nAll tests passed for both methods.")


if __name__ == "__main__":
    run_tests()

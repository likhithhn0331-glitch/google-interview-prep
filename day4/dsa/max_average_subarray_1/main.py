from brute_force import max_average_brute_force
from sliding_window import max_average_sliding_window


def run_tests():
    test_cases = [
        ([1, 12, -5, -6, 50, 3], 4),
        ([1, 2, 3, 4], 2),
        ([5], 1),
        ([1, 2, 3, 4, 5], 3),
        ([10, -2, -3, 4, 5], 2),
        ([-1, -2, -3, -4], 2),
        ([7, 7, 7, 7], 3),
        ([1, 3, -1, -3, 5, 3, 6, 7], 3),
        ([2, 2, 2, 2], 4),
        ([3, -1, 3, -1, 3], 2),
        ([1, 2, 3], 5),
        ([1, 2, 3], 0),
    ]

    print("Running Maximum Average Subarray 1 tests...\n")

    for idx, (array, k) in enumerate(test_cases, start=1):
        brute_result = max_average_brute_force(array, k)
        sliding_result = max_average_sliding_window(array, k)

        if brute_result is None or sliding_result is None:
            print(f"Test {idx}: array={array}, k={k}")
            print(f"  brute force: {brute_result}")
            print(f"  sliding window: {sliding_result}")
            print(f"  status: {'PASS' if brute_result == sliding_result else 'FAIL'}\n")
            continue

        match = abs(brute_result - sliding_result) < 1e-9
        print(f"Test {idx}: array={array}, k={k}")
        print(f"  brute force: {brute_result}")
        print(f"  sliding window: {sliding_result}")
        print(f"  status: {'PASS' if match else 'FAIL'}\n")

        if not match:
            raise AssertionError(
                f"Mismatch for array={array}, k={k}: brute={brute_result}, sliding={sliding_result}"
            )

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()

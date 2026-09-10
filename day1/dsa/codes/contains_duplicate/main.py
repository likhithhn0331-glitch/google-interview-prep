# Contains Duplicate DSA problem
from brute_force import contains_duplicate_brute_force
from set_method import contains_duplicate_set_method
import time
import random


def time_func(func, arr, runs=5):
    """Run func(arr) runs times and return (result, avg_elapsed_seconds)."""
    # Warm-up / correctness run
    result = func(arr)
    # Timing runs
    total = 0.0
    for _ in range(runs):
        t0 = time.perf_counter()
        func(arr)
        t1 = time.perf_counter()
        total += (t1 - t0)
    return result, total / runs


# LeetCode-style testcases
testcases = [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1,1,1,3,3,4,3,2,4,2], True),
]

# Add larger cases to compare performance
N = 2000
unique_large = list(range(N))               # expected: False
duplicate_at_end = unique_large + [0]       # expected: True (duplicate)
duplicate_early = [0] + list(range(1, N)) + [1]  # expected: True (duplicate early)

testcases += [
    (unique_large, False),
    (duplicate_at_end, True),
    (duplicate_early, True),
]

print(f"{'case':<30} {'set_res':<8} {'set_time(s)':<12} {'brute_res':<10} {'brute_time(s)':<12}")
print('-' * 80)
for arr, expected in testcases:
    # to reduce variance, shuffle a copy for some tests (but keep original for expected)
    arr_for_test = list(arr)  # shallow copy

    set_res, set_time = time_func(contains_duplicate_set_method, arr_for_test)
    brute_res, brute_time = time_func(contains_duplicate_brute_force, arr_for_test)

    name = (str(arr[:10]) + ("..." if len(arr) > 10 else ""))
    print(f"{name:<30} {str(set_res):<8} {set_time:<12.6f} {str(brute_res):<10} {brute_time:<12.6f}")

# Summary note
print('\nNote: times are averages over a few runs; brute force scales O(n^2), set method scales O(n).')

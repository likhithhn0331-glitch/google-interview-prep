#!/usr/bin/env python3
"""
Main test runner for Contiguous Array solutions.
Contains two implementations (brute-force and prefix-sum + hashmap) and a set of test cases.
"""
from typing import List, Tuple


def find_max_length_bruteforce(nums: List[int]) -> int:
    n = len(nums)
    best = 0
    for i in range(n):
        zeros = 0
        ones = 0
        for j in range(i, n):
            if nums[j] == 0:
                zeros += 1
            else:
                ones += 1
            if zeros == ones:
                best = max(best, j - i + 1)
    return best


def find_max_length_prefix(nums: List[int]) -> int:
    first_idx = {0: -1}
    running = 0
    best = 0
    for i, v in enumerate(nums):
        running += -1 if v == 0 else 1
        if running in first_idx:
            best = max(best, i - first_idx[running])
        else:
            first_idx[running] = i
    return best


TEST_CASES: List[Tuple[List[int], int]] = [
    ([0, 1], 2),
    ([0, 1, 0], 2),
    ([0, 0, 1, 1], 4),
    ([0, 0, 0, 1, 1, 1], 6),
    ([0, 0, 0, 0], 0),
    ([1, 1, 1, 1], 0),
    ([0, 1, 0, 1, 0, 1], 6),
    ([0], 0),
    ([], 0),
]


def run_tests():
    print("Running tests for Contiguous Array implementations:\n")
    for name, func in [("Brute-force", find_max_length_bruteforce), ("Prefix-sum", find_max_length_prefix)]:
        print(f"== {name} ==")
        all_pass = True
        for i, (inp, expected) in enumerate(TEST_CASES):
            out = func(inp)
            ok = out == expected
            all_pass = all_pass and ok
            status = "PASS" if ok else "FAIL"
            print(f"TC{i+1}: nums={inp} expected={expected} got={out} => {status}")
        print(f"Result: {'ALL PASS' if all_pass else 'SOME FAIL'}\n")


if __name__ == '__main__':
    run_tests()

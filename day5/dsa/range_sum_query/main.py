# DSA PROBLEM 3 — Range Sum Query — Immutable

class BruteForceNumArray:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        total = 0
        for i in range(left, right + 1):
            total += self.nums[i]
        return total


class PrefixSumNumArray:
    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)
        for i, value in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + value

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]


def run_test_case(nums, queries, label):
    brute = BruteForceNumArray(nums)
    prefix = PrefixSumNumArray(nums)

    for left, right in queries:
        expected = brute.sumRange(left, right)
        actual = prefix.sumRange(left, right)
        if expected != actual:
            raise AssertionError(
                f"{label} failed: nums={nums}, query=({left}, {right}), "
                f"expected={expected}, actual={actual}"
            )

    print(f"{label}: PASS")


def main():
    test_cases = [
        {
            "label": "basic positive numbers",
            "nums": [1, 2, 3, 4, 5],
            "queries": [(0, 0), (1, 3), (0, 4), (2, 4)],
        },
        {
            "label": "negative and mixed values",
            "nums": [-2, 0, 3, -5, 2, -1],
            "queries": [(0, 2), (2, 5), (0, 5), (1, 4)],
        },
        {
            "label": "single element",
            "nums": [7],
            "queries": [(0, 0)],
        },
        {
            "label": "all zeros",
            "nums": [0, 0, 0, 0],
            "queries": [(0, 3), (1, 2), (2, 3)],
        },
        {
            "label": "repeated queries",
            "nums": [10, -3, 4, 7],
            "queries": [(0, 3), (1, 3), (0, 0), (2, 2), (1, 2)],
        },
    ]

    for case in test_cases:
        run_test_case(case["nums"], case["queries"], case["label"])

    print("All test cases passed for both solutions.")


if __name__ == "__main__":
    main()

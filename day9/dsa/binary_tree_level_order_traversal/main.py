"""Test and compare the brute-force and queue-based implementations."""

from typing import Iterable, List, Optional

from brute_force import levelOrder as brute_force_level_order
from trees import TreeNode, levelOrder as queue_level_order


def build_tree(values: Iterable[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from level-order values using None for missing nodes."""
    values = list(values)
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = [root]
    index = 1

    while queue and index < len(values):
        node = queue.pop(0)

        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1

        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1

    return root


def run_tests() -> None:
    test_cases = [
        ("empty tree", [], []),
        ("single node", [1], [[1]]),
        ("example tree", [3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ("left-skewed tree", [5, 4, None, 3, None, 2], [[5], [4], [3], [2]]),
        ("right-skewed tree", [1, None, 2, None, 3], [[1], [2], [3]]),
        ("negative and duplicate values", [0, -1, -1, None, 2], [[0], [-1, -1], [2]]),
    ]

    for name, level_order, expected in test_cases:
        root = build_tree(level_order)
        brute_result = brute_force_level_order(root)
        queue_result = queue_level_order(root)

        assert brute_result == expected, (
            f"{name}: brute force returned {brute_result}, expected {expected}"
        )
        assert queue_result == expected, (
            f"{name}: queue solution returned {queue_result}, expected {expected}"
        )
        assert brute_result == queue_result, (
            f"{name}: implementations disagree: "
            f"{brute_result} != {queue_result}"
        )

        print(f"PASS: {name}: {queue_result}")

    print(f"\n{len(test_cases)} test cases passed.")


if __name__ == "__main__":
    run_tests()

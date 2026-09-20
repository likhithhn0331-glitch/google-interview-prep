"""Test and compare the brute-force and tree-DP implementations."""

from typing import Iterable, Optional

from brute_force import maxDepth as brute_force_max_depth
from trees import TreeNode, maxDepth as tree_max_depth


def build_tree(values: Iterable[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from level-order values using None for gaps."""
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
        ("empty tree", [], 0),
        ("single node", [7], 1),
        ("example tree", [3, 9, 20, None, None, 15, 7], 3),
        ("right-skewed tree", [1, None, 2, None, 3, None, 4], 4),
        ("left-skewed tree", [5, 4, None, 3, None, 2], 4),
        ("negative and duplicate values", [0, -1, -1, None, 2], 3),
        ("unbalanced tree", [1, 2, 3, 4, None, None, 5, 6], 4),
    ]

    for name, level_order, expected in test_cases:
        root = build_tree(level_order)
        brute_result = brute_force_max_depth(root)
        tree_result = tree_max_depth(root)

        assert brute_result == expected, (
            f"{name}: brute force returned {brute_result}, expected {expected}"
        )
        assert tree_result == expected, (
            f"{name}: tree solution returned {tree_result}, expected {expected}"
        )
        assert brute_result == tree_result, (
            f"{name}: implementations disagree: "
            f"{brute_result} != {tree_result}"
        )
        print(f"PASS: {name}: depth {tree_result}")

    print(f"\n{len(test_cases)} test cases passed.")


if __name__ == "__main__":
    run_tests()

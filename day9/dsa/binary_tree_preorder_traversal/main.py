"""Test and compare the recursive and iterative preorder implementations."""

from typing import Iterable, List, Optional

from brute_force import preorderTraversal as brute_force_preorder
from trees import TreeNode, preorderTraversal as iterative_preorder


def build_tree(values: Iterable[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from a level-order list using None for missing nodes."""
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
        ("single node", [7], [7]),
        ("right-skewed tree", [1, None, 2, 3], [1, 2, 3]),
        ("complete tree", [1, 2, 3, 4, 5], [1, 2, 4, 5, 3]),
        ("negative and duplicate values", [0, -1, -1, None, 2], [0, -1, 2, -1]),
        ("left-skewed tree", [5, 4, None, 3, None, 2], [5, 4, 3, 2]),
    ]

    for name, level_order, expected in test_cases:
        root = build_tree(level_order)
        brute_result = brute_force_preorder(root)
        iterative_result = iterative_preorder(root)

        assert brute_result == expected, (
            f"{name}: brute force returned {brute_result}, expected {expected}"
        )
        assert iterative_result == expected, (
            f"{name}: iterative returned {iterative_result}, expected {expected}"
        )
        assert brute_result == iterative_result, (
            f"{name}: implementations disagree: "
            f"{brute_result} != {iterative_result}"
        )

        print(f"PASS: {name}: {brute_result}")

    print(f"\n{len(test_cases)} test cases passed.")


if __name__ == "__main__":
    run_tests()


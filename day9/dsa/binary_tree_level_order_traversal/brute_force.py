"""Brute-force baseline for binary-tree level-order traversal."""

from typing import List, Optional


def levelOrder(root: Optional[object]) -> List[List[int]]:
    """Return values level by level by rescanning the tree for every depth.

    This approach is intentionally a baseline.  It first computes the tree
    height, then performs a depth-limited traversal once for each level.
    """
    if root is None:
        return []

    def height(node: Optional[object]) -> int:
        if node is None:
            return 0
        return 1 + max(height(node.left), height(node.right))

    def values_at_depth(node: Optional[object], depth: int) -> List[int]:
        if node is None:
            return []
        if depth == 0:
            return [node.val]
        return values_at_depth(node.left, depth - 1) + values_at_depth(
            node.right, depth - 1
        )

    result: List[List[int]] = []
    for depth in range(height(root)):
        result.append(values_at_depth(root, depth))
    return result

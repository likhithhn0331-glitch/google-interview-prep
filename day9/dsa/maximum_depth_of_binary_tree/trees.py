"""Binary-tree data structure and optimized maximum-depth solution."""

from typing import Optional


class TreeNode:
    """A node in a binary tree."""

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    """Return the maximum number of nodes on a root-to-leaf path."""
    if root is None:
        return 0

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return 1 + max(left_depth, right_depth)

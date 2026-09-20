"""Binary-tree data structure and queue-based level-order traversal."""

from collections import deque
from typing import Deque, List, Optional


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


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """Return node values level by level using breadth-first search."""
    if root is None:
        return []

    result: List[List[int]] = []
    queue: Deque[TreeNode] = deque([root])

    while queue:
        level_size = len(queue)
        level: List[int] = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        result.append(level)

    return result

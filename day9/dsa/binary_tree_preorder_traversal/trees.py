"""Tree data structure and iterative preorder traversal."""

from typing import List, Optional


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


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """Return values in Root -> Left -> Right order using an explicit stack."""
    if root is None:
        return []

    result: List[int] = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right first so left is processed first when the stack pops.
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

    return result


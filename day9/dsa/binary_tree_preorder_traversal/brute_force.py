"""Recursive baseline for binary-tree preorder traversal."""

from typing import List, Optional


def preorderTraversal(root: Optional[object]) -> List[int]:
    """Return values in Root -> Left -> Right order using recursion.

    This is the direct baseline: recursively visit every subtree while writing
    into one result list.
    """
    result: List[int] = []

    def visit(node: Optional[object]) -> None:
        if node is None:
            return
        result.append(node.val)
        visit(node.left)
        visit(node.right)

    visit(root)
    return result

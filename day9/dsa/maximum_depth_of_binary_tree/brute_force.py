"""Brute-force baseline for finding the maximum depth of a binary tree."""

from typing import List, Optional


def maxDepth(root: Optional[object]) -> int:
    """Enumerate every root-to-leaf path and return the longest path length.

    This is intentionally a baseline implementation.  It keeps a copy of the
    current path and compares path lengths when leaves are reached.
    """
    if root is None:
        return 0

    longest = 0

    def explore(node: Optional[object], path: List[int]) -> None:
        nonlocal longest
        if node is None:
            return

        path.append(node.val)
        if node.left is None and node.right is None:
            longest = max(longest, len(path))
        else:
            explore(node.left, path)
            explore(node.right, path)
        path.pop()

    explore(root, [])
    return longest

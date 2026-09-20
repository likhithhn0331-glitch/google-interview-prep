# DSA Problem — Maximum Depth of Binary Tree

## Problem Statement

Given the `root` of a binary tree, return its **maximum depth**.

The **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

A **leaf node** is a node that has no left or right child.

## Example 1

**Input:**

```text
root = [3,9,20,null,null,15,7]
```

**Binary Tree:**

```text
        3
       / \
      9   20
         /  \
        15   7
```

**Output:**

```text
3
```

**Explanation:**

The longest path is:

```text
3 → 20 → 15
```

or

```text
3 → 20 → 7
```

Both paths contain **3 nodes**, so the maximum depth is `3`.

## Example 2

**Input:**

```text
root = [1,null,2]
```

**Binary Tree:**

```text
    1
     \
      2
```

**Output:**

```text
2
```

## Example 3

**Input:**

```text
root = []
```

**Output:**

```text
0
```

**Explanation:**

An empty binary tree has a maximum depth of `0`.

## Constraints

* The number of nodes in the tree is in the range `[0, 10⁴]`.
* `-100 <= Node.val <= 100`.

## Function Signature

### Python

```python
def maxDepth(root: Optional[TreeNode]) -> int:
    pass
```

## Goal

Implement a function that returns the **maximum depth of the given binary tree**.

**Expected Time Complexity:** `O(n)`

**Expected Space Complexity:** `O(h)`, where `h` is the height of the tree.

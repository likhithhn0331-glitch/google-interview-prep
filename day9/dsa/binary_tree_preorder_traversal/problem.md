# Binary Tree Preorder Traversal

## Problem Statement

Given the `root` of a binary tree, return the **preorder traversal** of its nodes' values.

In a **preorder traversal**, the nodes are visited in the following order:

**Root → Left → Right**

## Example 1

**Input:**
```text
root = [1,null,2,3]
```

**Binary Tree:**
```text
    1
     \
      2
     /
    3
```

**Output:**
```text
[1,2,3]
```

## Example 2

**Input:**
```text
root = [1,2,3,4,5]
```

**Binary Tree:**
```text
        1
       / \
      2   3
     / \
    4   5
```

**Output:**
```text
[1,2,4,5,3]
```

## Example 3

**Input:**
```text
root = []
```

**Output:**
```text
[]
```

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Follow-up

Can you solve the problem using an **iterative approach** without recursion?

## Expected Function

```python
def preorderTraversal(root):
    pass
```

## Traversal Pattern

```text
Preorder
   ↓
Root
   ↓
Left Subtree
   ↓
Right Subtree
```

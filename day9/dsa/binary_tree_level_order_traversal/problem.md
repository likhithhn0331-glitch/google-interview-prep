# Binary Tree Level Order Traversal

## Problem Statement

Given the `root` of a binary tree, return the **level order traversal** of its nodes' values.

Level order traversal means visiting the nodes **level by level from left to right**, starting from the root.

## Example 1

**Input:**

```text
root = [3,9,20,null,null,15,7]
```

**Output:**

```text
[[3],[9,20],[15,7]]
```

**Explanation:**

* Level 1: `[3]`
* Level 2: `[9,20]`
* Level 3: `[15,7]`

## Example 2

**Input:**

```text
root = [1]
```

**Output:**

```text
[[1]]
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

* The number of nodes in the tree is in the range `[0, 2000]`.
* `-1000 <= Node.val <= 1000`

## Function Signature

### Python

```python
def levelOrder(root):
    # return the level order traversal
```

## Expected Approach

Use **Breadth-First Search (BFS)** with a **queue**.

At each step:

1. Store the number of nodes currently in the queue. This represents one level.
2. Process exactly those nodes.
3. Add their left and right children to the queue.
4. Store the values of the processed nodes as one level in the result.

## Complexity

* **Time:** `O(n)`, where `n` is the number of nodes.
* **Space:** `O(n)` for the queue and result.

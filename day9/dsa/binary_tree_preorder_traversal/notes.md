# Preorder Traversal Study Notes

The request refers to three problems, but this directory currently contains
one problem statement. To keep the notes useful and complete, the three
sections below cover three standard approaches to this problem.

## Problem

Return the node values of a binary tree in preorder: Root, then Left, then
Right. Return an empty list for an empty tree.

## Pattern

Depth-first search (DFS), specifically preorder traversal.

## Recognition signal

The required order explicitly says that a node must be processed before its
children, and the left subtree must be completed before the right subtree.
That is the definition of preorder DFS.

## Brute force

The direct baseline is recursive DFS. For each node, append the node value,
then recursively solve the left and right subtrees. This mirrors the problem
statement and is easy to prove correct.

## Why brute force is insufficient

Recursion uses the call stack. A tree shaped like a linked list can have
height `n`, which can exceed Python's recursion limit. The list-concatenation
version can also create unnecessary intermediate lists.

## Optimized idea

Replace implicit recursion with an explicit stack. Pop the next node, visit
it, push right, then push left. This preserves preorder while avoiding
recursion-depth failures.

## Invariant

Before every stack iteration, the stack contains exactly the unvisited nodes
needed to continue preorder, with the next node to visit at the top.

## Algorithm

1. If the root is `None`, return `[]`.
2. Initialize `stack = [root]` and an empty result list.
3. While the stack is not empty, pop a node and append its value.
4. Push its right child if present.
5. Push its left child if present.
6. Return the result.

## Dry run

For `[1, 2, 3, 4, 5]`, the tree is `1` with children `2` and `3`, and `2`
has children `4` and `5`:

| Action | Stack after action | Result |
| --- | --- | --- |
| Start | `[1]` | `[]` |
| Pop 1; push 3, 2 | `[3, 2]` | `[1]` |
| Pop 2; push 5, 4 | `[3, 5, 4]` | `[1, 2]` |
| Pop 4 | `[3, 5]` | `[1, 2, 4]` |
| Pop 5 | `[3]` | `[1, 2, 4, 5]` |
| Pop 3 | `[]` | `[1, 2, 4, 5, 3]` |

## Complexity

Recursive DFS takes `O(n)` time and `O(h)` call-stack space. The explicit
stack also takes `O(n)` time and `O(h)` auxiliary space. The output itself
requires `O(n)` space in either approach. Morris traversal below takes
`O(n)` time and `O(1)` auxiliary space.

## Edge cases

- Empty tree.
- Single-node tree.
- Only-left or only-right chains.
- Missing child between populated nodes.
- Negative, zero, or duplicate values.
- A tree at the maximum allowed node count.

## Common mistakes

- Pushing left before right, which visits the right subtree first.
- Returning node objects instead of node values.
- Forgetting the empty-tree check.
- Using a queue and accidentally implementing level-order traversal.
- Treating duplicate values as the same node.
- Failing to restore pointers when using Morris traversal.

## Alternative approach

Morris preorder traversal uses temporary right links from the predecessor of
the current node back to the current node. If a node has no left child, visit
it and move right. Otherwise, find the rightmost node in its left subtree:

- If its right link is empty, visit the current node, create the thread, and
  move left.
- If its right link already points to the current node, remove the thread and
  move right.

This gives `O(1)` auxiliary space but is less readable and temporarily
modifies the tree. It is useful when strict memory constraints matter.

## Interview follow-ups

### How do you prove the iterative algorithm?

Use the stack invariant: the top item is always the next preorder node.
Visiting it and pushing right before left preserves that invariant.

### What is the worst-case height?

`h = n` for a completely skewed tree, and `h = O(log n)` for a balanced tree.

### Can you avoid recursion?

Yes. Use the explicit stack implementation in `trees.py`.

### Can you avoid extra space entirely?

Morris traversal uses `O(1)` auxiliary space, but it temporarily changes
links and must restore them.

### How would you adapt this to return nodes?

Append the node references instead of `node.val`; the traversal order and
stack logic remain unchanged.

### How would you process values online?

Yield `node.val` when a node is popped instead of storing all values in a
result list. This reduces retained output memory when callers can consume an
iterator.


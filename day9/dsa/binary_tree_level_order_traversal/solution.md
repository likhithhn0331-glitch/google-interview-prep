# Binary Tree Level Order Traversal

## Problem

Given the root of a binary tree, return the node values level by level from
left to right.  An empty tree returns `[]`.

For example, the tree `[3, 9, 20, null, null, 15, 7]` produces
`[[3], [9, 20], [15, 7]]`.

## Solution 1: Brute-force depth scans

The baseline first computes the tree height.  For every depth, it recursively
scans the tree and collects nodes exactly at that depth.  This is easy to
derive from the definition of a level, but the same upper portions of the
tree are revisited for every level.

```python
def values_at_depth(node, depth):
    if node is None:
        return []
    if depth == 0:
        return [node.val]
    return values_at_depth(node.left, depth - 1) + \
        values_at_depth(node.right, depth - 1)
```

If `h` is the height, this can take `O(nh)` time.  In a skewed tree `h = n`,
so the worst case is `O(n^2)`.  The recursion depth is `O(h)`, and the output
requires `O(n)` space.

## Solution 2: Queue-based BFS (`trees.py`)

Breadth-first search naturally processes one level at a time:

1. Put the root in a queue.
2. Record the queue length; it is the number of nodes in the current level.
3. Remove exactly that many nodes, append their values to one level, and add
   their children to the queue.
4. Repeat until the queue is empty.

The `level_size` snapshot is important.  Children added during the loop belong
to the next level and must not be included in the current level.

### Correctness argument

Before each outer-loop iteration, the queue contains exactly the unprocessed
nodes at the next level, in left-to-right order.  Processing the saved
`level_size` nodes therefore visits every node in the current level in order.
Appending left children before right children preserves left-to-right order in
the next queue level.  Every node is enqueued and removed exactly once, so the
result contains every value in the required order.

### Complexity

For `n` nodes, BFS takes `O(n)` time.  The queue holds at most one level, so its
auxiliary space is `O(w)`, where `w` is the maximum width; `w` is `O(n)` in
the worst case.  The returned result itself also requires `O(n)` space.

## Comparison

| Approach | Time | Auxiliary space | Main tradeoff |
| --- | --- | --- | --- |
| Repeated depth scans | `O(nh)`, worst `O(n^2)` | `O(h)` recursion | Simple baseline, repeated work |
| Queue-based BFS | `O(n)` | `O(w)` queue | Optimal general solution |

## Interview questions and answers

### Why is this BFS rather than DFS?

BFS explores all nodes at distance `d` before any node at distance `d + 1`.
That is exactly the required level-by-level ordering. DFS follows a complete
branch before its siblings and therefore needs extra bookkeeping to group
values by depth.

### Why capture `len(queue)` before processing a level?

The queue initially contains only the current level.  As nodes are removed,
their children are appended.  Saving the original length ensures that those
new children are deferred to the next outer iteration.

### Why use `deque` instead of a list?

`deque.popleft()` is `O(1)`.  Removing index zero from a Python list shifts
all remaining elements and costs `O(n)` per removal, which can make traversal
quadratic.

### What is the difference between width and height?

Height `h` is the longest root-to-leaf path.  Width `w` is the largest number
of nodes at any single level.  BFS uses `O(w)` queue space; a recursive
depth-based solution uses `O(h)` call-stack space.

### What happens for a complete tree versus a skewed tree?

A complete tree can have a very wide middle level, so BFS may use `O(n)`
queue space.  A skewed tree has width one, so the BFS queue is `O(1)`, while
the brute-force scans can take `O(n^2)` time.

### Can the result be produced without storing every level?

Yes.  A generator can yield each completed level as soon as it is processed.
That reduces retained output memory for streaming callers, but the queue still
needs `O(w)` space.

### Can DFS solve the problem?

Yes.  A DFS can pass the current depth and append values into a list for that
depth.  It takes `O(n)` time and `O(h)` call-stack space, but BFS is usually
clearer because the requested order is level-based.

### What if the tree is too deep for recursion?

Use the iterative queue solution.  It does not depend on Python's recursion
limit and is robust for a highly skewed tree.

### Does the algorithm depend on unique values?

No.  Nodes are tracked by references, not by values, so negative and duplicate
values are preserved and each node is visited once.

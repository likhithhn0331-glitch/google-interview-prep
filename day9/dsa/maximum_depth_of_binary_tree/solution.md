# Maximum Depth of Binary Tree

## Problem

Given the root of a binary tree, return its maximum depth.  Depth is the
number of nodes on the longest path from the root to a leaf.  An empty tree
has depth `0`.

For example, `[3, 9, 20, None, None, 15, 7]` has maximum depth `3`:
`3 -> 20 -> 15` and `3 -> 20 -> 7` are both longest paths.

## Key observation

For any non-empty node, every path through that node contains the node itself,
then a longest path through either its left or right subtree:

```text
depth(node) = 1 + max(depth(node.left), depth(node.right))
```

The base case is `depth(None) = 0`.

## Solution 1: brute force path enumeration

`brute_force.py` explores every root-to-leaf path.  It appends the current
node to a mutable path, records the path length at a leaf, and removes the
node while backtracking.  The largest recorded length is the answer.

This is a useful baseline because it makes the definition of depth explicit:
depth is the length of a root-to-leaf path.  It also handles an empty tree
before starting the traversal.

### Correctness

Every root-to-leaf path is explored exactly once because each non-leaf node
recursively explores both children.  At each leaf, `path` contains exactly
the nodes from the root to that leaf.  Taking the maximum over all such paths
therefore returns the maximum depth.

### Complexity

With `n` nodes and height `h`, traversal takes `O(n)` time.  The current path
uses `O(h)` auxiliary space.  If path values must be copied or stored for
each leaf, the total bookkeeping can reach `O(nh)` in a highly branching
tree; this implementation avoids storing all paths, but still carries the
path values during traversal.

## Solution 2: recursive tree dynamic programming

`trees.py` computes the depth of each subtree once:

1. An empty subtree contributes `0`.
2. Recursively compute the left and right subtree depths.
3. Return `1 + max(left_depth, right_depth)`.

This is tree dynamic programming: the answer for a node is composed from
answers already computed for its children.

### Correctness proof

Use induction on the subtree:

- **Base case:** An empty subtree has no nodes, so returning `0` is correct.
- **Inductive step:** Assume the function correctly returns the maximum depth
  for both children.  Any root-to-leaf path through the current node chooses
  one child and has one additional node for the current root.  Therefore the
  longest path has length `1 + max(left_depth, right_depth)`.

Thus the function is correct for every binary tree.

### Complexity

Each node is visited once, so time complexity is `O(n)`.  The recursion stack
has one frame per level, so auxiliary space is `O(h)`, where `h` is the tree
height.  A balanced tree has `h = O(log n)`; a skewed tree has `h = O(n)`.

## Comparison

| Approach | Main idea | Time | Auxiliary space |
| --- | --- | --- | --- |
| Brute force | Enumerate root-to-leaf paths | `O(n)` traversal; path bookkeeping can be `O(nh)` | `O(h)` |
| Tree DP | Combine child depths at each node | `O(n)` | `O(h)` |

The tree-DP solution is preferred because it stores only the numeric answer
for each subtree and directly expresses the recurrence.  For a very deep
skewed tree, an iterative DFS or BFS avoids Python recursion-limit concerns.

## Interview questions and answers

### What does “depth” mean here: edges or nodes?

This problem defines depth as nodes.  Therefore an empty tree is `0`, a
single-node tree is `1`, and a root with one child is `2`.  If an interviewer
uses edge-based height instead, the base case and returned value change by one.

### Why do we use `max`, not `min` or a sum?

The problem asks for the longest root-to-leaf path.  A path continues through
one child, so we choose the larger child depth.  Summing would count nodes
from two different paths and would solve a different problem.

### What happens when one child is missing?

The missing child is an empty subtree with depth `0`.  For example, a node
with only a left child returns `1 + max(left_depth, 0)`, so the valid child
is naturally selected.

### Can the tree contain negative or duplicate values?

Yes.  Values do not affect depth, and the algorithm never compares node
values.  Duplicate values still belong to different node objects and are
traversed independently.

### Can you write an iterative solution?

Yes.  Use a stack containing `(node, depth)` pairs for DFS, or a queue
containing `(node, depth)` pairs for BFS.  Update the answer whenever a node
is removed.  Both visit each node in `O(n)` time; DFS uses `O(h)` typical
auxiliary space, while BFS uses `O(w)` queue space for maximum width `w`.

### How would you avoid recursion overflow?

Use the iterative DFS or BFS version.  Recursive space is `O(h)`, but a
skewed tree can have `h = 10^4`, which can exceed Python's recursion limit.
Increasing the recursion limit is less robust than removing the dependency on
the call stack.

### How would you find minimum depth?

Use BFS and stop at the first leaf, because BFS visits nodes in increasing
depth order.  A recursive solution can also take the minimum, but must treat a
missing child carefully: a node with one child cannot use `0` as the minimum
depth of a real path.

### How would you count the number of deepest leaves?

Return a pair `(depth, count)` from each subtree.  Keep the count from the
deeper child; if both child depths are equal, add their counts.  A leaf
returns `(1, 1)`, and an empty subtree returns `(0, 0)`.

### How would you return the actual deepest path?

Return the best path rather than only its length.  For each node, recursively
obtain the best child path, choose the longer one, and prepend the current
value.  This requires `O(h)` path storage per active recursion branch.

### What if the input is not a tree and contains cycles?

The recurrence assumes a finite acyclic binary tree.  If arbitrary object
graphs are possible, maintain a set of visited node identities to prevent
infinite traversal; that changes the problem and adds `O(n)` memory.

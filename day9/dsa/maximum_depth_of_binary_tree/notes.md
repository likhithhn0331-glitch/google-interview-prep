# Maximum Depth of Binary Tree Study Notes

The directory contains one problem statement.  The three solution-oriented
sections below cover the requested baseline, optimized solution, and a useful
iterative alternative.

## 1. Brute-force path enumeration

### Problem

Return the number of nodes on the longest root-to-leaf path.

### Pattern

Depth-first search with backtracking.

### Recognition signal

The phrase “longest path from the root to a leaf” suggests exploring each
candidate root-to-leaf path and comparing their lengths.

### Brute force

Maintain the current path, append a node when entering it, update the answer
when a leaf is reached, and pop the node while backtracking.

### Why brute force is insufficient

It carries path contents even though only the length is needed.  If complete
paths are copied or retained, bookkeeping can grow to `O(nh)`.  It also still
uses recursion, which can overflow on a skewed tree.

### Optimized idea

Return only the best numeric depth from each subtree instead of materializing
paths.

### Invariant

During backtracking, `path` contains exactly the nodes from the root of the
original tree to the current node.

### Algorithm

1. Return `0` for an empty tree.
2. Visit each node using DFS.
3. Append the node value.
4. At a leaf, compare `len(path)` with the best answer.
5. Otherwise explore both children, then remove the node.

### Dry run

For `1 -> left 2 -> left 3` and `1 -> right 4`:

```text
path [1]       -> branch
path [1, 2]    -> branch
path [1, 2, 3] -> leaf, best = 3
path [1, 4]    -> leaf, best remains 3
```

### Complexity

Traversal is `O(n)` time and `O(h)` active path space.  Copying/storing every
path can cost `O(nh)` total bookkeeping.

### Edge cases

Empty tree, one node, a one-sided chain, duplicate values, negative values,
and a root with only one child.

### Common mistakes

Forgetting to pop during backtracking, counting edges instead of nodes,
updating the answer at internal nodes, or treating a missing child as a leaf.

### Alternative approach

Use a breadth-first queue with each node's depth and retain the last depth.

### Interview follow-ups

Ask how path enumeration differs from returning only a scalar, how to return
the actual deepest path, and how to handle recursion depth.

## 2. Recursive tree dynamic programming

### Problem

Compute maximum depth from the answers of the left and right subtrees.

### Pattern

Postorder DFS / tree dynamic programming.

### Recognition signal

The answer for a node is a fixed formula over its children:
`1 + max(left answer, right answer)`.

### Brute force

Enumerate root-to-leaf paths first, then keep only the largest length.

### Why brute force is insufficient

It performs work to maintain path contents that the recurrence does not need,
and path copies can add avoidable overhead.

### Optimized idea

Summarize each subtree by one integer: its maximum depth.

### Invariant

When `maxDepth(node)` returns, it equals the maximum number of nodes on any
path from `node` to a leaf.

### Algorithm

1. If `node` is `None`, return `0`.
2. Recursively compute both child depths.
3. Return `1 + max(left_depth, right_depth)`.

### Dry run

For `[3, 9, 20, None, None, 15, 7]`:

```text
depth(9)  = 1
depth(15) = 1, depth(7) = 1
depth(20) = 1 + max(1, 1) = 2
depth(3)  = 1 + max(1, 2) = 3
```

### Complexity

`O(n)` time and `O(h)` auxiliary recursion space.  Balanced trees use
`O(log n)` stack space; skewed trees use `O(n)`.

### Edge cases

Empty tree returns `0`; a leaf returns `1`; missing children contribute `0`;
values have no effect on the answer.

### Common mistakes

Using `min` instead of `max`, summing child depths, returning `0` for a leaf,
or confusing node depth with edge height.

### Alternative approach

Iterative DFS with `(node, depth)` pairs or iterative BFS by levels.

### Interview follow-ups

Discuss a correctness induction, recursion limits, minimum depth, deepest
leaf count, and returning the actual deepest path.

## 3. Iterative traversal alternative

### Problem

Find the greatest depth reached while traversing every node.

### Pattern

Stack-based DFS or queue-based BFS.

### Recognition signal

The input can be deep enough that recursive call-stack space is unsafe.

### Brute force

Use recursive path enumeration or recursive tree DP.

### Why brute force is insufficient

Python recursion may fail for a linked-list-shaped tree even though the
algorithmic recurrence is correct.

### Optimized idea

Store the current depth alongside each pending node in an explicit container.

### Invariant

Every pending `(node, depth)` pair contains the node's true depth from the
root, and the answer is the greatest depth already removed from the container.

### Algorithm

1. Return `0` for an empty root.
2. Push `(root, 1)` onto a stack.
3. Pop a pair, update the answer, and push children with `depth + 1`.
4. Return the greatest depth after the stack is empty.

### Dry run

For `1` with children `2` and `3`, and `2` with child `4`:

```text
stack [(1, 1)] -> pop 1, push (2, 2), (3, 2)
pop (2, 2)     -> push (4, 3), answer 2
pop (4, 3)     -> answer 3
pop (3, 2)     -> final answer 3
```

### Complexity

Each node is processed once: `O(n)` time.  DFS uses `O(h)` stack space in the
usual case; BFS uses `O(w)` space, where `w` is maximum tree width.

### Edge cases

Empty input, a single node, all-left and all-right chains, and a wide tree.

### Common mistakes

Pushing a child at the same depth, forgetting either child, using `pop(0)` on
a list for BFS, or assuming the last visited node is always deepest.

### Alternative approach

Use the recursive tree-DP recurrence when the height is known to be safe, or
level-order BFS and count levels.

### Interview follow-ups

Compare DFS and BFS memory, explain when BFS is preferable, and adapt the
traversal to find minimum depth or the rightmost deepest leaf.

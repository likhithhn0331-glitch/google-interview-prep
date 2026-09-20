# Binary Tree Level Order Traversal Study Notes

## Problem

Return the values of a binary tree level by level from left to right.  Return
an empty list when the root is `None`.

## Pattern

Breadth-first search (BFS), using a queue and a level boundary.

## Recognition signal

The words “level order,” “by depth,” or “left to right on each level” signal
that all nodes at one distance from the root must be processed before moving
deeper.

## Brute force

Compute the tree height, then run a depth-limited traversal separately for
each depth.  When the requested depth reaches zero, record the node value.
This is the direct baseline implemented in `brute_force.py`.

## Why brute force is insufficient

Each depth scan revisits ancestors and parts of subtrees already explored.
The repeated work costs `O(nh)` time, becoming `O(n^2)` for a skewed tree.
Recursive scans can also exceed the recursion limit on very deep inputs.

## Optimized idea

Use a queue.  At the beginning of each iteration, the queue contains exactly
one level.  Save its size, process those nodes, and enqueue their children for
the next level.

## Invariant

At the start of every outer-loop iteration, the queue contains all and only
the unprocessed nodes in the next level, in left-to-right order.

## Algorithm

1. Return `[]` if the root is `None`.
2. Enqueue the root.
3. Save the current queue size as the level size.
4. Remove exactly that many nodes, recording values and enqueueing children.
5. Append the completed level to the result.
6. Repeat until the queue is empty.

## Dry run

For `[3, 9, 20, None, None, 15, 7]`:

| Action | Queue after action | Result |
| --- | --- | --- |
| Start | `[3]` | `[]` |
| Process level size 1 | `[9, 20]` | `[[3]]` |
| Process level size 2 | `[15, 7]` | `[[3], [9, 20]]` |
| Process level size 2 | `[]` | `[[3], [9, 20], [15, 7]]` |

## Complexity

The queue solution visits each node once: `O(n)` time.  Its auxiliary queue
uses `O(w)` space, where `w` is maximum level width, and the output uses
`O(n)` space.  The brute-force baseline uses `O(nh)` time and `O(h)` recursive
stack space, excluding the output.

## Edge cases

- Empty tree.
- Single-node tree.
- Only-left or only-right chains.
- Missing children in the middle of a level.
- Negative, zero, and duplicate values.
- The maximum allowed node count.

## Common mistakes

- Processing `while queue` without saving the level size.
- Enqueuing `None` children and accidentally treating them as nodes.
- Using `list.pop(0)`, which is slower than `deque.popleft()`.
- Returning one flat list instead of one list per level.
- Assuming node values are unique.
- Reversing child insertion order and losing left-to-right traversal.

## Alternative approach

Depth-first search can carry the current depth and append to `result[depth]`.
It remains `O(n)` time and uses `O(h)` recursion stack space, but it is less
direct for this ordering.  A two-queue or sentinel-marker BFS is also valid,
though capturing `len(queue)` is usually the clearest boundary technique.

## Interview follow-ups

### How would you return the tree's zigzag level order?

Process each level normally, then reverse every other level (or use a deque
for the current level).  The traversal still needs the same queue boundary.

### How would you return the right-side view?

At each level, retain the last node processed.  The queue traversal already
provides the required level boundaries, so this is `O(n)` time.

### How would you find the minimum depth?

Stop at the first dequeued leaf.  BFS reaches nodes in increasing depth, so
the first leaf is guaranteed to have minimum depth.

### How would you serialize the tree?

Use BFS and emit each node value, including a marker for missing children when
needed to preserve structure.  Trim only trailing missing markers if the
serialization format permits it.

### Can the queue space be reduced?

Not generally while retaining ordinary BFS order: a wide level must be held
until it is processed.  DFS can use `O(h)` auxiliary space, but it changes the
traversal strategy.

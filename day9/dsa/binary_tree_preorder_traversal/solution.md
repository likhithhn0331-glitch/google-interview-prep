# Binary Tree Preorder Traversal

## Problem

Given the root of a binary tree, return the values of all nodes in preorder:

```text
Root -> Left subtree -> Right subtree
```

An empty tree returns an empty list. The input can contain negative and
duplicate values; values are not used to identify nodes.

## Solution 1: Recursive baseline (`brute_force.py`)

The most direct implementation follows the definition of preorder traversal.
For a non-empty node, append its value, recursively traverse the left child,
and then recursively traverse the right child. A `None` child contributes an
empty list.

```python
def preorderTraversal(root):
    if root is None:
        return []
    return (
        [root.val]
        + preorderTraversal(root.left)
        + preorderTraversal(root.right)
    )
```

This is called the brute-force/baseline solution here because it directly
follows the recursive definition and uses the language call stack. It is
correct and often the clearest first solution, but a highly skewed tree can
exceed Python's recursion limit.

## Solution 2: Iterative tree-stack traversal (`trees.py`)

Use an explicit stack containing nodes still waiting to be visited:

1. Put the root on the stack.
2. Pop one node and append its value.
3. Push its right child, then its left child.
4. Repeat until the stack is empty.

Because a stack is last-in, first-out, pushing right before left guarantees
that left is visited next.

```python
def preorderTraversal(root):
    if root is None:
        return []

    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return result
```

This directly answers the follow-up asking for an iterative solution and does
not modify the input tree.

## Correctness argument

At each loop iteration, the stack contains pending nodes in reverse order of
their required preorder processing. The top node is therefore the next node
in preorder. After visiting it, placing its right child below its left child
preserves the same property for both subtrees. Once the stack is empty, every
reachable node has been visited exactly once, so `result` is the preorder
traversal.

## Complexity

Let `n` be the number of nodes and `h` the tree height.

| Approach | Time | Auxiliary space | Notes |
| --- | --- | --- | --- |
| Recursive baseline | `O(n)` | `O(h)` call stack | Can hit recursion depth limits |
| Iterative stack | `O(n)` | `O(h)` stack | Output list is `O(n)` and is not counted as auxiliary space |

The iterative method is generally preferable in Python because it avoids
recursion-depth failures. In the worst case of a skewed tree, `h = n`; for a
balanced tree, `h = O(log n)`.

## Edge cases

- `root is None` returns `[]`.
- A single node returns a one-element list.
- A tree with only left children still visits top to bottom.
- A tree with only right children still visits top to bottom.
- Negative, zero, and duplicate values are preserved exactly.

## Interview questions and answers

### Why is the right child pushed before the left child?

The stack is LIFO. Pushing right first and left second leaves left on top,
so the next pop follows Root -> Left -> Right.

### What changes for inorder or postorder traversal?

Inorder is Left -> Root -> Right, so the iterative version needs to delay
visiting a node until its left side has been processed. Postorder is
Left -> Right -> Root, so it needs either two stacks, a visited-state marker,
or a carefully managed one-stack algorithm.

### Can the traversal be done with `O(1)` auxiliary space?

Yes, Morris preorder traversal temporarily rewires right pointers to create
threads back to ancestors. It runs in `O(n)` time and `O(1)` auxiliary space,
but it mutates the tree temporarily and is more complex. The pointers must
be restored before returning.

### Why not use breadth-first search?

BFS visits by depth (level order), not by subtree order. A queue would produce
a different sequence and does not match Root -> Left -> Right.

### Does the algorithm work when values are duplicated?

Yes. Traversal follows node references, not value comparisons, so every node
is visited once even when values are equal.

### What is the maximum stack size?

At most `O(h)`. A balanced tree has a small stack relative to `n`; a
right-skewed tree has at most one pending node at a time, while branching
trees can retain nodes from ancestor right subtrees.

### How would you test the two implementations?

Use an empty tree, one node, balanced trees, left- and right-skewed trees,
missing children, negative values, and duplicates. Compare both outputs with
known expected results and assert that the two implementations agree. The
included `main.py` does exactly that.

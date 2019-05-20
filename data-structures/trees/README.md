# Trees
- trees are widely used data structure
- a tree is made out of Nodes with zero or several references to other nodes

## Vocabulary
1. **Root**: a top-level node that is guaranteed to have a path to every other node
2. **Parent**
3. **Child**
4. **Descendant**: all the nodes that can be reached by following a path of child nodes
5. **Ancestor**: any other node for which the node is a descendant
6. **Leaves**: the leaves are nodes that do not have any children

## Binary Trees
- each node has no more than two children - commonly referred to as RIGHT and LEFT
- Binary Tree depth is roughly: **log N**

## Binary Search Trees
- the value held by a node’s left child is <= to its own value
- the value held by a node’s right child is >= to its value
- used to eliminate parts of the search base for a more efficient search

### Balanced vs. Unbalanced Tree
- the absolute difference between left subtree height and right subtree height cannot be greater than 1

### **Complete Binary Tree**
- every level of the tree is fully filled, except for perhaps the last level (always left to right)

> It can be represented as an array: Parent position n -> Children 2n+1 & Children 2n+2

### **Full Binary Tree**
- every node has zero or two children - no nodes with only one children

### **Perfect Binary Tree**
- both full and complete - all leaf nodes are at the same level

## Time complexity of operations

| Algorithm | Average                                            | Worst case                  |
| --------- | -------------------------------------------------- | --------------------------- |
| Storage   | O(n) each element requires a Node                  | O(n) tree looks like a tree |
| Search    | O(log n) eliminate half search space on every move | O(n) tree looks like a tree |
| Insert    | O(log n) eliminate half search space on every move | O(n) tree looks like a tree |
| Delete    | O(log n) eliminate half search space on every move | O(n) tree looks like a tree |

# Tree Traversal Algorithms

## In-order Traversal
- the left subtree is visited first, then the root and later the right sub-tree (lnr)

## Pre-order Traversal
- the root node is visited first, then the left subtree and finally the right subtree (nlr)

## Post-order Traversal
- the left node is visited first, then the right subtree and finally the root node (lrn)

# Heap
- it is a `complete binary tree` -> it is constructed row by row from left to right
- max efficient implementation of a priority queue ADT
- used for sorting

> Abstract Data Type(ADT) - core API that caracterizes a data type

## Operations
- insert an item with priority
- pull the highest priority item
- is empty?
- peek

## Time complexity of operations

| Algorithm | Average  | Worst case |
| --------- | -------- | -----------|
| Storage   | O(n)     | O(n)       |
| Search    | O(n)     | O(n)       |
| Insert    | O(1)     | O(log n)   |
| Delete    | O(log n) | O(log n)   |
| Peek      | O(1)     | O(1)       |

## Min-Heap
- the parent is always smaller or equal than it's children
- the root is the minimum element

## Max-Heap
- the parent is always greater or equal than it's children
- the root is the maximum element

# Graph Search
- fundamental search methodologies for searching relationships

## Depth First Search
- uses a stack - LIFO
- it can be done recursively
- it goes deep into a path -> explores -> comes back -> decides if it will go on a different path
- Uses: backtracking, complete search, exhausting path possibilities

## Breadth First Search
- uses a queue - FIFO
- it can be done iteratively
- check if there is a path between 2 nodes
- it goes wide, slowly increasing the distance from the start node

# Stack

- a last-in-first-out (LIFO) data structure = the item most recently added to the stack will first be removed

## Operations
- push: add element
- pop: remove element
- peek: retun the top of the stack
- isEmpty

## Stack using a Link List
PROS:
- no hard size limit
- easy to implement: no bounds checking
- empty list = empty stack

CONS:
- memory allocation on push
- per-node memory overhead
- potential performance issues (data locality & memory fragmentation)

## Stack using an Array

# Queue

- a first-in first-out (FIFO) data structure = items are removed from the data structure in the same order they are added

## Operations
- add: add element
- remove: remove element
- peek: retun the top of the queue

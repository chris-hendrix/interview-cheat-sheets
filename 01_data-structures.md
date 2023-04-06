# Data structures

## Big O
| | index | search | opt search | insert| append | sort |
| --- | --- | --- | --- | --- | --- | --- |
| array | **`O(1)`** | `O(n)` | **`O(logn)`** | `n/a` | `n/a` | `O(n*logn)` |
| dynamic array | **`O(1)`** | `O(n)` | **`O(logn)`** | `O(n)` | **`O(1)`** | `O(n*logn)` |
| linked list | `O(n)` | `O(n)` | `O(n)` | `O(n)` | **`O(1)`** | `O(n*logn)` |
| hash | **`O(1)`** | `O(n)` | `O(n)` | **`O(1)`** | `n/a` | `O(n*logn)` |
| binary tree | `O(logn)` | **`O(logn)`** | **`O(logn)`** | `O(logn)` | `O(logn)` | **`O(n)`** |
| min heap | `O(logn)` | **`O(logn)`** | **`O(logn)`** | `O(logn)` | `O(logn)` | `O(n*logn)` |

## Arrays
### Overview
- Optimal for indexing; bad at searching, inserting, and deleting (except at the end)
- **Dynamic array**: doubles in size when max is met (copies n elements so `O(n)`)
### Time complexity
- Indexing:         Linear array: `O(1)`   
- Search:           Linear array: `O(n)` 
- Optimized Search: Linear array: `O(log n)`
- Insertion:        Dynamic array: `O(n)` 

## Linked list, stack, queue
### Overview
- Optimal for insertion and deletion, slow at indexing and searching
- **Stack**: LIFO, linked list that inserts at head, removes from head
- **Queue**: FIFO, linked list that adds to tail, removes from head
### Complexity
- Indexing:         Linked Lists: `O(n)`
- Search:           Linked Lists: `O(n)`
- Optimized Search: Linked Lists: `O(n)`
- Append:           Linked Lists: `O(1)`
- Prepend:          Linked Lists: `O(1)`
- Insertion:        Linked Lists: `O(n)`
```
from collections import deque
stack = deque([1, 2, 3])
stack.appendleft(5)  # adds at head
stack.popleft()  # gets from head
# deque([1, 2, 3])

queue = deque([1, 2, 3])
queue.append(5)  # adds to end
queue.popleft()  # gets from head
# queue deque([2, 3, 5])
```

## Hash table
### Overview
- Storage with key value pairs
- Handle collisions in linked list
### Complexity
- Indexing:         Hash Tables: `O(1)`
- Search:           Hash Tables: `O(1)`
- Insertion:        Hash Tables: `O(1)`

## Trees
### Overview
- Node with left and right node
- Designed for searching and sorting
- Maximum number of nodes (perfect) is `2^depth`
- Types
  - **Binary search tree**: `left <= parent < right`, no duplicate nodes
  - **Balanced**: balanced enough for `O(logn)` traversal
  - **Complete**: super balanced, `abs(nleft-nright) <= 1`
  - **Full**: all nodes have 0 or 2 children
  - **Perfect**: full and complete

### Traversal
| | in-order | pre-order | post-order |
|--- | --- | --- | --- |
recursive order | `left-curr-right` | `curr-left-right` | `left-right-curr` |
order | BST smallest to largest | root is always first | root is always last

### Complexity
- Indexing:  Binary Search Tree: `O(log n)`
- Search:    Binary Search Tree: `O(log n)`
- Insertion: Binary Search Tree: `O(log n)`

## Heaps (trees)
### Overview
- Complete unordered tree with root is the minimum
- Guarantees `O(logn)` search (BST does not)
- Can use `queue.PriorityQueue`, props: `get()`, `put()`, `qsize()`, `queue`
- Ordering takes 
- Represented by array
  - current: `arr[i]`
  - parent: `arr[(i-1)/2]`
  - left: `arr[(2*i) + 1]`
  - right: `arr[(2*i )+ 2]`

### Complexity
- Indexing:   Min Heap: `O(log n)`
- Search:     Min Heap: `O(log n)`
- Insertion:  Min Heap: `O(log n)`
- Heapify:    Min Heap: `O(n*logn)`
- Sort:       Min Heap: `O(n*logn)`
# Algorithms

## Search
### Binary search (sorted arrays)
- takes smaller and smaller jumps in the array until value is found (must be sorted)
```
def binary_search(x, arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
```
- **Complexity**: `O(logn)`
### BFS (trees, graphs)
- Used for shortest path (no need to visit every node, shallow trees)
- Uses recursion
- More memory that depth first (queue storage)
- **Complexity**
  - Trees (traversal): `O(n)` or `O(sqrtn)`/`O(logn)` for avg/balanced
  - Graphs: `O(V+E)` (vertices and edges)

```
def bfs(node):
    adj = {}
    q = deque([node])
    while len(q) > 0:
        curr = q.popleft()
        adj[curr.val] = []
        for child in curr.children:
            adj[curr.val].append(child.val)
            if not child.val in adj:  # not visited
                q.append(child)
    return adj
```
### DFS (trees, graphs)
- Used to visit every node (deep trees)
- Uses queue
- **Complexity**
  - Trees (traversal): `O(n)` or `O(sqrtn)`/`O(logn)` for avg/balanced
  - Graphs: `O(V+E)` (vertices and edges)
```
def dfs(node, adj={}):
    if not node:
        return
    adj[node.val] = []
    for child in node.children:
        adj[node.val].append(child.val)
        if not child.val in adj:   # not visited
            dfs(child, adj)
    return adj
```

## Sorting
| Algorithm | Worst | Average | Best | Memory |
| --- | --- | --- | --- | --- |
| Bubble | `O(n2)` | `O(n2)` | `O(n2)` | `O(1)` |
| Selection | `O(n2)` | `O(n2)` | `O(n2)` | `O(1)` |
| Merge | `O(nlogn)` | `O(nlogn)` | `O(n)` | `O(n)` |
| Quick | `O(n2)` | `O(nlogn)` | `O(nlogn)` | `O(logn)` |
### Bubble sort
- Takes n passes and swap elements until sorted
- Largest will bubble up at end

### Selection sort
- Swaps min and first "untouched" element

### Merge sort
- Splits array in half and **recursively** and merges the two list
- Need merge AND sort function
```
def merge_sort(arr):
    if len(arr) < 2:
        return
    mid = len(arr) // 2
    left, right = arr[0:mid], arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, arr)
```

### Quick sort
- moves each element before or after a random pivot (recursion)
- partition function rearranges and returns the partition index
```
def quicksort(arr, start=None, end=None):
    start = 0 if start is None else start 
    end = len(arr) - 1 if end is None else end
    if start >= end: 
        return
    p = partition(arr, start, end)
    quicksort(arr, start, p-1)
    quicksort(arr, p+1, end)
```



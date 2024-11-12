# Algorithms

## Search
### Binary search (sorted arrays)
- takes smaller and smaller jumps in the array until value is found (must be sorted)
```
def binary_search(x, arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
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
- Uses queue
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
- Uses recursion
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

### Bellman Ford (weighted graphs)
- Finds the shortest distance to all nodes from a starting node
- Can't handle negative distances
- **Complexity**
  - `O(V*E)`
```
def bellman_ford(source, vertices, edges):
    distances = {v: float('inf') for v in vertices}
    distances[source] = 0

    for _ in range(len(vertices) - 1):
        for start, end, weight in edges:
            distances[end] = min(distances[end], distances[start] + weight)
   return distances
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

### Quicksort
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

### Dynamic programming
- Fibonacci creates runs in `O(2^n)` (two branches per node), DP improves it to `O(n)`
```
def fib_dp(n, memo={}):
    if n < 2:
        return n
    if not n in memo:
        memo[n] = fib_dp(n - 1) + fib_dp(n - 2)
    return memo[n]
```

### Bit manipulation
- **Operations**
    | Operation | Python | Notes
    | --------------- | -----   | ------------------------------------------------- |
    | **AND**         | `a & b` | Both are 1, then 1, otherwise 0                   |
    | **OR**          | `a | b` | One is 1, then 1, otherwise 0                     |
    | **XOR**         | `a ^ b` | Sum is 1 then 0, otherwise 1                      |
    | **NOT**         | `~a `   | All are opposite                                  |
    | **Left Shift**  | `a << n`| Arith shift left n spaces, fill with zeros (\*2n) |
    | **Right Shift** | `a >> n`| Arith shift right n spaces, remove smaller (/2n)  |

- **Two's complement**: leading zero represents positive/negative, to convert to negative: flip bits and add 1, then add switch leading bit to 1
    | 4-bit | Unsigned | Signed |
    | --- | --- | --- |
    | `00` | `0` | `0` |
    | `01` | `1` | `1` |
    | `10` | `2` | `-1` |
    | `11` | `3` | `0` |
- **Hexadecimal**: base 16 (0-F, 0-F), 1 byte (8 bits), `0xFF = 16*16 = 1111111`
- **Common functions**
```
                                # i = 2
def get_ith_bit(x, i):          # x = 1011 (7)
    m = 1 << i                  # m = 0100 AND
    return = x & m != 0         # r = 0000 != 0  (= false = 0)

def set_ith_bit_to_one(x, i)    # x = 1011 (7)
    m = 1 << i                  # m = 0100 OR
    return x | m                # r = 1111

def set_ith_bit_to_zero(x, i)   # x = 1111 (15)
    m = 1 << i                  # m = 0100 NOT
    m = ~m                      # m = 1011 AND
    return m & m                # r = 1011
```

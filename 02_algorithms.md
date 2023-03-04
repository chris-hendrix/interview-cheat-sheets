# Algorithms

## Search
### BFS (breadth first search)
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
### DFS (depth first search)
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

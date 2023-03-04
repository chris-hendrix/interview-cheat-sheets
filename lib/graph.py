from collections import deque
import random
import networkx as nx
import matplotlib.pyplot as plt


class GraphNode:
    def __init__(self, val):
        self.val = val
        self.parents = []
        self.children = []
        self.visited = False

    def add_child(self, node):
        self.children.append(node)
        node.parents.append(self)

    def remove_child(self, node):
        node.parents.remove(self)
        self.children.remove(node)

    def __str__(self):
        return str({
            'val': self.val,
            'children': str([c.val for c in self.children]),
            'parents': str([c.val for c in self.parents]),
            'visited': self.visited
        })


class Graph:
    DEFAULT_N = 6
    DEFAULT_MAX_CHILDREN = 3
    DEFAULT_MIN = 0
    DEFAULT_MAX = 10

    @staticmethod
    def plot_graph(adj):
        G = nx.DiGraph(adj)
        nx.draw_networkx(G)
        plt.show()

    @staticmethod
    def adj_to_graph(adj):
        nodes = {}
        for val in adj.vals():
            nodes[val] = GraphNode(val)

        for val in adj.vals():
            for n in adj[val]:
                nodes[val].children.append(nodes[n])
        return list(nodes.values())[0]

    @staticmethod
    def random_graph(n=DEFAULT_N, max_children=DEFAULT_MAX_CHILDREN,
                     min_val=DEFAULT_MIN, max_val=DEFAULT_MAX):
        node_vals = random.sample(range(min_val, max_val + 1), n)
        node = GraphNode(node_vals.pop())
        q = deque([node])
        n_nodes = 1

        while len(q) > 0 and len(node_vals) > 0:
            curr = q.popleft()
            nodes_left = len(node_vals) - n_nodes
            n_children = random.randint(0, min(max_children, nodes_left))
            child_vals = [node_vals.pop() for _ in range(n_children)]
            for val in child_vals:
                child = GraphNode(val)
                curr.add_child(child)
                q.append(child)
        return node

    @staticmethod
    def dfs(node, adj={}):
        if not node:
            return
        adj[node.val] = []
        for child in node.children:
            adj[node.val].append(child.val)
            visited = child.val in adj
            if not visited:
                Graph.dfs(child, adj)
        return adj

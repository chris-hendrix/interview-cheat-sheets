import random


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.parent = None

    def insert(self, val):
        if self.val == val:
            return
        elif self.val < val:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)
            self.right.parent = self
        else:  # self.val > val
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
            self.left.parent = self

    def add_left(self, val):
        self.left = TreeNode(val)
        self.left.parent = self
        return self.left

    def add_right(self, val):
        self.right = TreeNode(val)
        self.right.parent = self
        return self.right

    def __str__(self):
        return str({
            'val': self.val,
            'left_val': self.left.val if self.left != None else None,
            'right_val': self.right.val if self.right != None else None,
            'parent_val': self.parent.val if self.parent != None else None
        })

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        '''Returns list of strings, width, height, and horizontal coordinate of the root.'''
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class Tree:
    DEFAULT_N = 6
    DEFAULT_MIN = 0
    DEFAULT_MAX = 10

    @staticmethod
    def bst_from_list(arr):
        '''generates a bst from a list'''
        tree = None
        for val in arr:
            if tree == None:
                tree = TreeNode(val)
            tree.insert(val)
        return tree

    @staticmethod
    def get_random_node(root, max_steps=10):
        '''gets a random node from a tree'''
        curr = root
        steps = random.randint(1, max_steps)
        for i in range(0, steps):
            go_left = random.randint(0, 1) == 0 and curr.left != None
            if go_left:
                curr = curr.left
            elif curr.right != None:
                curr = curr.right
            else:
                break
        return curr

    @staticmethod
    def random_tree(n=DEFAULT_N, min=DEFAULT_MIN, max=DEFAULT_MAX):
        '''generates a non-bst tree of n elements'''
        root = TreeNode(random.randint(min, max))
        node = root
        for _ in range(n - 1):
            insert_left = random.randint(0, 1) == 0
            value = random.randint(min, max)
            if insert_left:
                if node.left != None:
                    node = node.left
                node.add_left(value)
                if node.right != None:
                    node = node.left
            else:
                if node.right != None:
                    node = node.right
                node.add_right(value)
                if node.left != None:
                    node = node.right
        return root

    @staticmethod
    def random_bst(n=DEFAULT_N, min=DEFAULT_MIN, max=DEFAULT_MAX):
        '''generates a random bst of n elements'''
        b = TreeNode(random.randint(min, max))
        for _ in range(n - 1):
            b.insert(random.randint(min, max))
        return b

    @staticmethod
    def random_balanced_bst(n=DEFAULT_N, min=DEFAULT_MIN, max=DEFAULT_MAX):
        '''generates a random bst of n elements'''
        node = Tree.random_bst(n, min, max)
        return Tree.balanced_bst(node)

    @staticmethod
    def balanced_bst(node):
        arr = []
        Tree.in_order(node, arr)
        return Tree.balanced_bst_from_list(arr)

    @staticmethod
    def balanced_bst_from_list(arr):
        if not arr:
            return None

        # get middle node
        mid = len(arr) // 2
        root = TreeNode(arr[mid])

        # recursively get left and right half of tree
        root.left = Tree.balanced_bst_from_list(arr[0:mid])
        root.right = Tree.balanced_bst_from_list(arr[mid + 1:])

        return root

    @staticmethod
    def in_order(node, results=[]):
        '''gets the vals of the tree from least to greatest (left->curr->right)'''
        if node == None:
            return
        Tree.in_order(node.left, results)
        results.append(node.val)
        Tree.in_order(node.right, results)
        return results

    @staticmethod
    def pre_order(node, results=[]):
        '''gets the vals of the tree with the root first (curr->left->right)'''
        if node == None:
            return
        results.append(node.val)
        Tree.pre_order(node.left, results)
        Tree.pre_order(node.right, results)
        return results

    @staticmethod
    def post_order(node, results=[]):
        '''gets the vals of the tree with the root last (left->right->curr)'''
        if node == None:
            return
        Tree.post_order(node.left, results)
        Tree.post_order(node.right, results)
        return results

    @staticmethod
    def build_min_heap(arr):
        '''builds min heap tree from array'''
        # https://www.askpython.com/python/examples/min-heap
        nodes = [TreeNode(arr[i]) for i in range(1, len(arr))]
        nodes = list(filter(lambda n: n.key != None, nodes))
        nodes.insert(0, None)
        cursize = len(nodes) - 1
        node = None
        for i in range(cursize // 2, 0, -1):
            # create node
            node = nodes[i]

            # get child indices (1-based)
            ileft = 2 * i
            iright = 2 * i + 1

            # set children
            if ileft <= cursize:
                node.left = nodes[ileft]
            if iright <= cursize:
                node.right = nodes[iright]
        return node

class ListNode:
    def __init__(self, val=None, next=None, head=True):
        if head:
            self.head = self
        self.val = val
        self.next = next
        self.prev = None

    def move_next(self):
        self.next = ListNode()
        self.next.head = self.head
        self.prev = self
        return self.next

    def __repr__(self):
        arr = []
        node = self.head
        while node:
            arr.append(str(node.val))
            node = node.next
        return f'({"->".join(arr)})'


class LinkedList:
    @staticmethod
    def create_from_arr(arr):
        if not arr or len(arr) < 0:
            return None
        head = node = ListNode(arr[0])
        for val in arr[1:]:
            node.next = ListNode(val)
            node = node.next
        return head

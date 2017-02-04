

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def connect(self, node):
        tail = dummy = TreeLinkNode(0)
        while node:
            tail.next = node.left
            if tail.next:
                tail = tail.next
            tail.next = node.right
            if tail.next:
                tail = tail.next
            node = node.next
            if not node:
                tail = dummy
                node = dummy.next



a = TreeLinkNode(1)
b = TreeLinkNode(2)
c = TreeLinkNode(3)
d = TreeLinkNode(4)
e = TreeLinkNode(5)
f = TreeLinkNode(6)
g = TreeLinkNode(7)
h = TreeLinkNode(8)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
d.left = g
f.right=h

s = Solution()
s.connect(a)

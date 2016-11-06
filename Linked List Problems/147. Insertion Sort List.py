# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        if not head or not head.next: return head
        d1,d2 = ListNode(0),ListNode(0)
        d1.next = head
        while d1.next:
            if not d2.next:
                d2.next = d1.next
                d1.next = d1.next.next
                d2.next.next = None
            elif d1.next.val <= d2.next.val:
                tmp = d1.next
                d1.next = d1.next.next
                tmp.next = d2.next
                d2.next = tmp
            else:
                tmp1 = d1.next
                d1.next = d1.next.next
                prev = d2.next
                current = d2.next.next
                while current and current.val <= tmp1.val:
                    prev = current
                    current = current.next
                if current is None:
                    prev.next = tmp1
                    tmp1.next = None
                else:
                    tmp2 = prev.next
                    prev.next = tmp1
                    tmp1.next = tmp2
                    
                
        return d2.next



a = ListNode(3)
b = ListNode(4)
c = ListNode(1)
a.next = b
b.next = c
s = Solution()
d2 = s.insertionSortList(a)

while d2:
    print d2.val
    d2 = d2.next

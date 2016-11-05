# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None: return head
        d1 = ListNode(0)
        d2 = ListNode(0)
        d1.next = head
        
        while d1.next:
            t1 = d1.next
            d1.next = t1.next
            t2 = d2.next
            d2.next = t1
            t1.next = t2
        return d2.next
        
        

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:return head
        d1,d2 = ListNode(0),ListNode(0)
        d1.next = head
        current = d2
        try:
            while d1.next:
                t1 = d1.next
                t2 = t1.next
                d1.next = t2.next
                current.next = t2
                current = current.next
                current.next = t1
                current = current.next
                current.next = None
        except Exception: 
            current.next = d1.next
            
        return d2.next
            
        

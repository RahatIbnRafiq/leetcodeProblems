# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        d1,d2,d3 = ListNode(0),ListNode(0),ListNode(0)
        d1.next, d2.next = l1,l2
        cur = d3
        while d1.next and d2.next:
            if d1.next.val <= d2.next.val:
                cur.next = d1.next
                d1.next = d1.next.next
            else:
                cur.next = d2.next
                d2.next = d2.next.next
            cur = cur.next
        if d1.next is not None:
            cur.next = d1.next
            d1.next = None
        elif d2.next is not None:
            cur.next = d2.next
            d2.next = None
        return d3.next
                
            
        

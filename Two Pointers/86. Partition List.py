# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        d1,d2,d3 = ListNode(0),ListNode(0),ListNode(0)
        d1.next = head
        cur2,cur3 = d2,d3
        while d1.next:
            tmp = d1.next
            d1.next = d1.next.next
            if tmp.val < x:
                cur2.next = tmp
                cur2 = cur2.next
                cur2.next = None
            else:
                cur3.next = tmp
                cur3 = cur3.next
                cur3.next = None
        cur2.next = d3.next
        return d2.next
                
        

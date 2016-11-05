# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        if not head: return None
        d1,d2 = ListNode(0),ListNode(0)
        d1.next = head
        current = None
        while d1.next:
            if d1.next.val == val:
                d1.next = d1.next.next
            else:
                if current:
                    current.next = d1.next
                    d1.next = d1.next.next
                    current = current.next
                    current.next = None
                else:
                    d2.next = d1.next
                    d1.next = d1.next.next
                    current = d2.next
                    current.next = None
                    
        return d2.next
                
        

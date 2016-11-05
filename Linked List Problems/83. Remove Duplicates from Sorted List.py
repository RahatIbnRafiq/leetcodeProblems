# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if head is None: return None
        d1,d2 = ListNode(0),ListNode(0)
        d1.next = head
        current = None
        while d1.next:
            if current is None:
                d2.next = d1.next
                d1.next = d1.next.next
                current = d2.next
                current.next = None
            elif current and current.val < d1.next.val:
                current.next = d1.next
                d1.next = d1.next.next
                current = current.next
                current.next = None
            else:
                d1.next = d1.next.next
        return d2.next
                
        
        

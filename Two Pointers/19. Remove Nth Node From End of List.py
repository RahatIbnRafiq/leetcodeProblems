# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head is None: return head
        dummy =ListNode(0)
        dummy.next = head
        fast = head
        while n:
            fast = fast.next
            n-=1
        slow = dummy
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        
        return dummy.next
        
        

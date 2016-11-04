# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None or head.next is None: return False
        slow,fast = head,head.next
        while True:
            try:
                if slow == fast:return True
                else: slow,fast = slow.next,fast.next.next
            except Exception: return False
        return False
        

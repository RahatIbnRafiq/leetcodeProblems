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
        
    def isPalindrome(self, head):
        if not head or not head.next: return True
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        p1,p2 = head,slow.next
        slow.next = None
        p3 = self.reverseList(p2)
        while p1 and p3 and p1.val == p3.val:
            p1,p3 = p1.next,p3.next
        if p1 is None and p3 is None: return True
        elif p1 is not None and p1.next is None and p3 is None: return True
        return False
        
        
        

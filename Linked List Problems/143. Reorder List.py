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
        
    def reorderList(self, head):
        if not head or not head.next: return
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        p1,p2 = head,slow.next
        slow.next = None
        p3 = self.reverseList(p2)
        
        d1,d2,d3 = ListNode(0),ListNode(0),ListNode(0)
        d1.next, d2.next = p1,p3
        
        current = d3
        
        while d1.next and d2.next:
            t1,t2 = d1.next.next,d2.next.next
            current.next = d1.next
            current = current.next
            current.next = d2.next
            current = current.next
            current.next =None
            d1.next,d2.next = t1,t2
        if d1.next is not None:
            current.next = d1.next
        elif d2.next is not None:
            current.next = d2.next
        d1.next = d3.next
            
        

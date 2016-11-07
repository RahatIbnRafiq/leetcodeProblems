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
        
        
    def reverseKGroup(self, head, k):
        d1,d2,d3 = ListNode(0),ListNode(0),ListNode(0)
        d1.next = head
        prev = d1
        cur3 = d3
        while d1.next:
            count = 1
            while count <= k and d1.next:
                tmp = d1.next
                d1.next = d1.next.next
                tmp2 = d2.next
                d2.next = tmp
                tmp.next = tmp2
                count +=1
            if count == k+1:
                cur3.next = d2.next
                while cur3.next:
                    cur3 = cur3.next
                d2.next = None
            else:
                cur3.next = self.reverseList(d2.next)
                while cur3.next:
                    cur3 = cur3.next
                d2.next = None
                return d3.next
        return d3.next
            
                
            
        

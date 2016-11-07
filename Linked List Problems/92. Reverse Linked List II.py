# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        d1,d2,d3,d4 = ListNode(0),ListNode(0),ListNode(0),ListNode(0)
        d1.next = head
        prev = d1
        l = 1
        cur2,cur3,cur4 = d2,d3,d4
        while d1.next:
            tmp = d1.next
            d1.next = d1.next.next
            if l < m:
                cur2.next = tmp
                cur2 = cur2.next
                cur2.next = None
            elif l > n:
                cur4.next = tmp
                cur4 = cur4.next
                cur4.next = None
            else:
                tmp2 = cur3.next
                cur3.next = tmp
                tmp.next = tmp2
            l+=1
        
        cur3 = d3.next
        while cur3.next:
            cur3 = cur3.next
        cur3.next = d4.next
        cur2.next = d3.next
        return d2.next
        
                
            
                
            
        

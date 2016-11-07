# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        d1,d2,d3 = ListNode(0),ListNode(0),ListNode(0)
        d1.next,d2.next,cur = l1,l2,d3
        carry = 0
        while d1.next or d2.next or carry:
            if not d1.next: 
                val1 = 0
            else:
                tmp = d1.next
                d1.next = d1.next.next
                tmp.next = None
                val1 = tmp.val
            
            
            if not d2.next: 
                val2 = 0
            else:
                tmp = d2.next
                d2.next = d2.next.next
                tmp.next = None
                val2 = tmp.val
            
            
            res = (val1+val2+carry)
            carry = res/10
            val = res%10
            node = ListNode(val)
            cur.next = node
            cur = cur.next
        return d3.next
            
                
        

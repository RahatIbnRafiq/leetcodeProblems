# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
            
        
        
        head = ListNode(0)
        s = 0
        
        while len(s1) > 0 or len(s2) > 0:
            if len(s1): 
                s+= s1.pop()
            if len(s2):
                s+= s2.pop()
            node = ListNode(s%10)
            s = s/10
            node.next = head.next
            head.next = node
        if s != 0:
            node = ListNode(s)
            node.next = head.next
            head.next = node
        return head.next
            
        

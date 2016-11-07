# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        d1,d2 = ListNode(0),ListNode(0)
        d1.next = head
        cur2 = d2
        
        while d1.next:
            p1 = d1.next
            p2 = d1.next.next
            count = 0
            while p2 and p2.val == p1.val:
                count+=1
                p2 = p2.next
            if count > 0:
                d1.next = p2
            else:
                tmp = d1.next
                d1.next = d1.next.next
                cur2.next = tmp
                cur2 = cur2.next
                cur2.next = None
        return d2.next
        

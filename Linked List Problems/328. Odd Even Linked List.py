# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next: return head
        d1,d2,d3 = ListNode(0),ListNode(0),ListNode(0)
        d1.next = head
        flag = 1
        currentOdd,currentEven = d2,d3
        while d1.next:
            if flag:
                tmp = d1.next
                d1.next = d1.next.next
                currentOdd.next = tmp
                currentOdd = tmp
                currentOdd.next = None
                flag = 0
            else:
                tmp = d1.next
                d1.next = d1.next.next
                currentEven.next = tmp
                currentEven = tmp
                currentEven.next = None
                flag = 1
        currentOdd.next = d3.next
        return d2.next
                
                
                
        

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def getSize(self,root):
        p1 = root
        length = 0
        while p1:
            length +=1
            p1 = p1.next
        return length
    def splitListToParts(self, root, k):
        N = self.getSize(root)
        listsWithExtra = N%k
        normalListSize = N/k
        results = []
        cur = root
        for i in xrange(k):
            temp = []
            for j in xrange(normalListSize):
                temp.append(cur.val)
                cur = cur.next
            if listsWithExtra > 0:
                temp.append(cur.val)
                cur = cur.next
                listsWithExtra -= 1
            results.append(temp)
        return results
        

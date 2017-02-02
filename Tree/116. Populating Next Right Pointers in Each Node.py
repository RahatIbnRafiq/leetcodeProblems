# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:return
        traversal = [[root]]
        level = 0
        while True:
            temp = []
            for node in traversal[level]:
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            if len(temp) < 1:break
            else: 
                traversal.append(temp)
                level +=1
        for l in traversal:
            for i in range(0,len(l)-1):
                l[i].next = l[i+1]
        

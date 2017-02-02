# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def countNodes(self,node):
        if not node:return 0
        return 1+self.countNodes(node.left)+self.countNodes(node.right)
    def kthSmallest(self, root, k):
        if not root:return root
        while True:
            left = self.countNodes(root.left)
            if left+1 == k: return root.val
            if left+1 > k: root = root.left
            else: 
                root = root.right
                k = k-left-1
        return None
        

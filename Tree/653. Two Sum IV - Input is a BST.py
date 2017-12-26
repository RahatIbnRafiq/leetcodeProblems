# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self,root,k,m):
        if not root:
            return False
        if (k-root.val) in m:
            return True
        else:
            m[root.val] = True
            if self.helper(root.left,k,m): return True
            if self.helper(root.right,k,m): return True
            return False
        
    def findTarget(self, root, k):
        return self.helper(root,k,dict())
        
        

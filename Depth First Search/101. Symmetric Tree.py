# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self,left,right):
        if left is None and right is None:return True
        if left is None or right is None:return False
        if left.val != right.val: return False
        return self.helper(left.left,right.right) and self.helper(left.right,right.left)
    def isSymmetric(self, root):
        if not root:return True
        return self.helper(root.left,root.right)
        

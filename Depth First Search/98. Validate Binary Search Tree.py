# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def helper(self,root,maxi,mini):
        if not root:return True
        if root.val < maxi and root.val > mini:
            return self.helper(root.left,root.val,mini) and self.helper(root.right,maxi,root.val)
        return False
    def isValidBST(self, root):
        return self.helper(root,sys.maxint,-sys.maxint - 1)
        

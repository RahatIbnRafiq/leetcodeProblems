# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self,root,origin,targets):
        if root is None:return 0
        hit = 0
        for t in targets:
            hit += ((t-root.val)==0)
        targets = [t-root.val for t in targets]+[origin]
        return hit+self.helper(root.left,origin,targets)+self.helper(root.right,origin,targets)
    def pathSum(self, root, sum):
        return self.helper(root,sum,[sum])

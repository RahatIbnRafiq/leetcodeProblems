# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            if t1.left and t2.left:
                root.left = self.mergeTrees(t1.left, t2.left)
            else:
                root.left = t1.left or t2.left
            
            if t1.right and t2.right:
                root.right = self.mergeTrees(t1.right, t2.right)
            else:
                root.right = t1.right or t2.right
            return root
        else:
            return t1 or t2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    best = 0
    def depth(self,root):
        if not root:return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        self.best = max(self.best,left+right)
        return 1+max(left,right)
    def diameterOfBinaryTree(self, root):
        if not root:return 0
        self.depth(root)
        return self.best

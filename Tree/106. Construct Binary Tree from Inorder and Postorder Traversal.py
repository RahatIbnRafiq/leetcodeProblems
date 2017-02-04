# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        if len(inorder):
            val = postorder.pop()
            node = TreeNode(val)
            index = inorder.index(val)
            node.right = self.buildTree(inorder[index+1:],postorder)
            node.left = self.buildTree(inorder[0:index],postorder)
            return node
        

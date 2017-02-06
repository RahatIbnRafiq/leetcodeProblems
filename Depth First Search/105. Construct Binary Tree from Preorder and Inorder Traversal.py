# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(inorder):
            val = preorder.pop(0)
            node = TreeNode(val)
            index = inorder.index(val)
            node.left = self.buildTree(preorder,inorder[0:index])
            node.right = self.buildTree(preorder,inorder[index+1:])
            return node
        

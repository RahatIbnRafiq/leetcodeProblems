# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getHeight(self,node):
        if not node:return 0
        return 1+self.getHeight(node.left)
    def countNodes(self, root):
        if not root:return 0
        leftH = self.getHeight(root.left)
        rightH = self.getHeight(root.right)
        if leftH == rightH:
            return (2**leftH)+self.countNodes(root.right)
        else:
            return (2**rightH)+self.countNodes(root.left)
            
        

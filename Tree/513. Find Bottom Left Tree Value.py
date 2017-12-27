# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        queue = [root]
        for node in queue:
            if node.right and node.left:queue+=[node.right,node.left]
            elif node.left or node.right: queue+=[node.right or node.left]
        return queue[-1].val
        

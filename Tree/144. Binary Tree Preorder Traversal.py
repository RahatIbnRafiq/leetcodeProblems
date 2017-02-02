# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        if not root:return []
        stack = []
        pre = []
        stack.append(root)
        
        while len(stack):
            node = stack.pop()
            pre.append(node.val)
            if node.right:stack.append(node.right)
            if node.left:stack.append(node.left)
        return pre
        
        

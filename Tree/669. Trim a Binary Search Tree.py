# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self,node,L,R):
        if not node:
            return None
        if node.val > R:
            return self.helper(node.left,L,R)
        elif node.val < L:
            return self.helper(node.right,L,R)
        else:
            node.left = self.helper(node.left,L,R)
            node.right = self.helper(node.right,L,R)
            return node
    def trimBST(self, root, L, R):
        return self.helper(root,L,R)
        
        

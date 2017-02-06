# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def helper(self,node):
        if not node:
            return (0, 0)
        l_yes, l_no = self.helper(node.left)
        r_yes, r_no = self.helper(node.right)
        return node.val + l_no + r_no, max(l_yes, l_no) + max(r_yes, r_no)
        
    def rob(self, node):
        return max(self.helper(node))
        
        

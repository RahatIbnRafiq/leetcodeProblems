# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def tree2str(self, t):
        if not t:
            return ""
        elif t.left is None and t.right is None:
            return str(t.val)
        elif t.right is None:
            return str(t.val)+"("+self.tree2str(t.left)+")"
        else:
            return str(t.val)+"("+self.tree2str(t.left)+")("+self.tree2str(t.right)+")"
        
        

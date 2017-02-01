# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    d = None
    def dfs(self,node):
        if node:
            self.d[node.val] = self.d.get(node.val,0)+1
            self.dfs(node.left)
            self.dfs(node.right)
        
    def findMode(self, root):
        if not root:return []
        self.d = dict()
        self.dfs(root)
        mode = max([self.d[key] for key in self.d.keys()])
        return [key for key in self.d.keys() if self.d[key] == mode]
        
        

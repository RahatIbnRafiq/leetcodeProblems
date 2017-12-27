# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self,root):
        if not root:
            return 0
        else:
            val = root.val + self.helper(root.left)+self.helper(root.right)
            self.d[val] = self.d.get(val,0)+1
            return val
            
    def findFrequentTreeSum(self, root):
        if not root: return []
        self.d = dict()
        self.helper(root)
        m = max(self.d.values())
        return [key for key in self.d.keys() if self.d[key] == m]

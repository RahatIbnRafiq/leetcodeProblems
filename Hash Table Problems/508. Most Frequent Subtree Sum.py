# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution(object):
    def helper(self,root):
        if not root:
            return 0
        val = self.helper(root.left)+self.helper(root.right)+root.val
        self.ctr[val]+=1
        return val
    def findFrequentTreeSum(self, root):
        self.ctr = collections.Counter()
        if root == None: return []
        self.helper(root)
        frequent = max(self.ctr.values())
        return [i for i in self.ctr.keys() if self.ctr[i] == frequent]
        
        

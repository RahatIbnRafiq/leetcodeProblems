# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        count = collections.Counter()
        ans = []
        def dfs(node):
            if not node:
                return "#"
            s = "{},{},{}".format(node.val,dfs(node.left),dfs(node.right))
            count[s] += 1
            if count[s] == 2:
                ans.append(node)
            return s
        dfs(root)
        return ans
        
        

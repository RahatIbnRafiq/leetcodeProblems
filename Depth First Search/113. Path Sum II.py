# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self,path,root,val):
        if root:
            if not root.left and not root.right and val == root.val:
                self.result.append(path+[root.val])
                return
            if root.left:
                self.helper(path+[root.val],root.left,val-root.val)
            if root.right:
                self.helper(path+[root.val],root.right,val-root.val)
            
    def pathSum(self, root, sum):
        self.result = []
        if root:
            self.helper([],root,sum)
        return self.result
        

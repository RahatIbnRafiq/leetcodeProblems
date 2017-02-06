# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def helper(self,root,path):
        if not root.left and not root.right:
            self.result.append(path+str(root.val))
            return
        if root.left:
            self.helper(root.left,path+str(root.val))
        if root.right:
            self.helper(root.right,path+str(root.val))
    def sumNumbers(self, root):
        self.result = []
        if not root:return 0
        if not root.left and not root.right:return root.val
        self.helper(root,"")
        return sum([int(x) for x in self.result])
        

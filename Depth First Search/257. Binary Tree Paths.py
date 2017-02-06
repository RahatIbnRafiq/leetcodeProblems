# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    result = None
    
    def helper(self,root,path):
        if root.left is None and root.right is None:
            self.result = self.result + [path+str(root.val)]
        if root.left:
            self.helper(root.left,path+str(root.val)+"->")
        if root.right:
            self.helper(root.right,path+str(root.val)+"->")
            
            
    def binaryTreePaths(self, root):
        if not root:return []
        self.result = []
        self.helper(root,"")
        print self.result
        return self.result
    
        

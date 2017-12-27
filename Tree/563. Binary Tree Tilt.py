# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = 0
    def helper(self,root):
        if not root:return 0
        else:
            if root.left and root.right:
                left,right = self.helper(root.left),self.helper(root.right)
            elif root.left:
                left,right = self.helper(root.left),0
            elif root.right:
                left,right = 0,self.helper(root.right)
            else:
                left,right = 0,0
            self.res+= abs(left-right)
            return root.val+left+right
            
                
        
    def findTilt(self,root):
        self.helper(root)
        return self.res
        
        
        

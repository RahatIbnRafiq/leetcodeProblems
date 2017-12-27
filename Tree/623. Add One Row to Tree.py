# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self,root,v,d,depth):
        if not root:
            return None
        else:
            if depth == d-1:
                t = root.left;
                root.left = TreeNode(v);
                root.left.left = t;
                t = root.right;
                root.right = TreeNode(v);
                root.right.right = t;
            else:
                self.helper(root.left,v,d,depth+1)
                self.helper(root.right,v,d,depth+1)
    def addOneRow(self, root, v, d):
        if d == 1:
            t = TreeNode(v)
            t.left = root
            return t
        else:
            self.helper(root,v,d,1)
            return root
        

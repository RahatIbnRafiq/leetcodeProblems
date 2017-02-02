# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMin(self,node):
        while node.left:
            node = node.left
        return node
    def deleteNode(self, root, key):
        if not root:return root
        if key < root.val: root.left = self.deleteNode(root.left,key)
        elif key > root.val: root.right = self.deleteNode(root.right,key)
        else:
            if not root.left: return root.right
            elif not root.right:return root.left
            else:
                node = self.findMin(root.right)
                root.val = node.val
                root.right = self.deleteNode(root.right,root.val)
        return root
                
        

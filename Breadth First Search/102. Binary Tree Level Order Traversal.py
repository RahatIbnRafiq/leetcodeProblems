# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        if not root:return []
        traversal = [[root]]
        level = 0
        while True:
            temp = []
            for node in traversal[level]:
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            if len(temp) < 1:break
            else: 
                traversal.append(temp)
                level +=1
        return [[x.val for x in y] for y in traversal]
            

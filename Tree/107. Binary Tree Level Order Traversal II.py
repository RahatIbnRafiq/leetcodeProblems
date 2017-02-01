# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        if root is None: return []
        result = [[root]]
        while True:
            temp = []
            for node in result[0]:
                if node.left: temp +=[node.left]
                if node.right: temp +=[node.right]
            if len(temp) > 0:
                result.insert(0,temp)
            else:
                break
        return [[y.val for y in x]for x in result]
            
        

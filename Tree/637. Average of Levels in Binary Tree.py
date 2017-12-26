# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        if not root:
            return [0]
        result = []
        stack = [[root]]
        
        while stack:
            temp = []
            l = stack.pop()
            s = 0.0
            c = 0.0
            for node in l:
                s+= float(node.val)
                c+=1.0
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            result.append(s/c)
            if len(temp) > 0:
                stack.append(temp)
            else:
                break
        return result
            
        

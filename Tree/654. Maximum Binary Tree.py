# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        m = max(nums)
        idx = nums.index(m)
        root = TreeNode(m)
        root.left = self.constructMaximumBinaryTree(nums[0:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return root
        

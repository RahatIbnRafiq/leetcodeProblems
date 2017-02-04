class Solution(object):
    def inorderTraversal(self, root):
        result, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:return result
            node = stack.pop()
            result.append(node.val)
            root = node.right
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, upper):
            if not node:
                return 0

            res = 1 if node.val >= upper else 0
            upper = max(upper, node.val)
            res += dfs(node.left, upper)
            res += dfs(node.right, upper)
            return res
        return dfs(root, root.val)
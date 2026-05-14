# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxval = root.val
        def max_path_sum(node):
            if not node:
                return 0
            leftsum = max(0, max_path_sum(node.left))
            rightsum = max(0, max_path_sum(node.right))
            currsum = leftsum + node.val + rightsum
            self.maxval = max(currsum, self.maxval)
            return node.val + max(leftsum, rightsum)
        max_path_sum(root)
        return self.maxval
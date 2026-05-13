# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        q = collections.deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                e = q.popleft()
                level.append(e.val)
                if e.left: q.append(e.left)
                if e.right: q.append(e.right)
            result.append(level[-1])
        return result
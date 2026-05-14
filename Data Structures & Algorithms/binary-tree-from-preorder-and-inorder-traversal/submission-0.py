# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {val:idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0
        def build(lower, upper):
            if lower > upper:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            mid = inorder_dict[root_val]
            root.left = build(lower, mid-1)
            root.right = build(mid+1, upper)
            return root
        return build(0, len(preorder)-1)
            
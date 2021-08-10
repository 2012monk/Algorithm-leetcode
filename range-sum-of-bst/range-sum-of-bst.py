# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        l = self.rangeSumBST(root.left, low, high)
        r = self.rangeSumBST(root.right, low, high)
        s = l + r
        if low <= root.val <= high:
            s += root.val
        return s
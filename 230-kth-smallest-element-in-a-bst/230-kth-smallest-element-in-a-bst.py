# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def f(node, left):
            if not node:
                return left
            l = f(node.left, left)
            node.idx = l + 1
            r = f(node.right, node.idx)
            return r
        def g(node, idx):
            if node.idx == idx:
                return node.val
            if node.idx > idx:
                return g(node.left, idx)
            return g(node.right, idx)
        f(root, 0)
        return g(root, k)

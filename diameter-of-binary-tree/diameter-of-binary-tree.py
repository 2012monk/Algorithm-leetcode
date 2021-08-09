# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    path: int = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return -1
            l, r = dfs(node.left), dfs(node.right)
            self.path = max(self.path, l+r+2)
            return max(l, r) + 1
        dfs(root)
        return self.path
            
        
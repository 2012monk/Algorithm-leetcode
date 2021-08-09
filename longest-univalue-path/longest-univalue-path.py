# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result: int = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            
            if node.left and node.left.val == node.val:
                l += 1
            else:
                l = 0
            if node.right and node.right.val == node.val:
                r += 1
            else:
                r = 0
            
            self.result = max(self.result, l+r)
            return max(l, r)
            
            
            
        dfs(root)
        
        return self.result
            
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def f(node, mx, mn):
            if not node:
                return 1
            if node.val >= mx or node.val <= mn:
                return 0
            ret = 1

            if node.left:
                ret = ret and node.left.val < node.val and f(node.left, min(mx, node.val), mn)
            if node.right:
                ret = ret and node.right.val > node.val and f(node.right, mx, max(node.val, mn))
            return ret
        return f(root, 1<<31, -(1<<31)-1)
    
            
            
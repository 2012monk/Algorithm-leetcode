# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r=[]
        def f(node):
            if not node:
                return
            
            f(node.left)
            r.append(node.val)
            f(node.right)
        f(root) 
        return r
        
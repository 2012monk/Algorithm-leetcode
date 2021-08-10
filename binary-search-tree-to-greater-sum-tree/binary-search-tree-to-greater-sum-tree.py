# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    acc: int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            root.val = self.acc = root.val + self.acc
            self.bstToGst(root.left)
        return root
            
#         def dfs(root, acc):
#             if not root:
#                 return 0
#             o = root.val
#             root.val += acc
#             s = dfs(root.right, acc)
#             l = dfs(root.left, acc+s + o)
#             root.val += s
#             return s + l + o
#         dfs(root, 0)
#         return root
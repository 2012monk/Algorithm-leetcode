# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            
            
            def draw(pre, ino):
                if not ino:
                    return
                node = TreeNode(pre[0])
                i = ino.index(pre[0])
                pre.pop(0)
                node.left = draw(pre, ino[:i])
                node.right = draw(pre, ino[i+1:])
                return node
            return draw(preorder, inorder)
                    
                    
            

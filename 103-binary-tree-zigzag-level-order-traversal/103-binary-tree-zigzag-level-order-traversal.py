# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = defaultdict(list)
        
        def f(node, lvl):
            if not node:
                return
            if lvl % 2 == 0:
                result[lvl].append(node.val)
            else:
                result[lvl].insert(0, node.val)
            f(node.left, lvl + 1)
            f(node.right, lvl + 1)
            

        f(root, 0) 
        return list(result.values())
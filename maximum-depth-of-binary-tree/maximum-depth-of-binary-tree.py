# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth = 0
        mq = deque([root])
        while mq:
            q = mq.copy()
            mq.clear()
            while q:
                n = q.popleft()
                if n.left:
                    mq.append(n.left)
                if n.right:
                    mq.append(n.right)
            
            depth += 1
            
        
        return depth
            
        
        
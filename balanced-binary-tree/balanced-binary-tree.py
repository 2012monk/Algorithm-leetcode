# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True
        def dfs(node):
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1
            return max(l, r) + 1

        return dfs(root) != -1
    
        q = deque([root])
        count = 1
        if not root:
            return True
        while q:
            for _ in range(len(q)):
                c = q.popleft()
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
            x = 1 << count
            if x != len(q) and x // 2 != len(q) and len(q) != 0:
                return False
            count += 1
        return True
                
            
        # return flag
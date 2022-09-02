"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        q = {}
        
        def f(node, lvl):
            if not node:
                return
            if lvl in q:
                q[lvl].next = node
            q[lvl]= node
            f(node.left, lvl + 1)
            f(node.right, lvl + 1)
        f(root, 0)
        return root

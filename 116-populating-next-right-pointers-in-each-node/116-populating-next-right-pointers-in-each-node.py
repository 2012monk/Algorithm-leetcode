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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
            
        m = defaultdict(list)
        def f(node, lvl):
            if not node:
                return
            m[lvl].append(node)
            f(node.left, lvl + 1)
            f(node.right, lvl + 1)
        
        f(root, 0)
        for a in m.values():
            for i in range(len(a) - 1):
                a[i].next = a[i + 1]
        return root
            
            
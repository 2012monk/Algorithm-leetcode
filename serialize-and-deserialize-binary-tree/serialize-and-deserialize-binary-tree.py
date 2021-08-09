# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        saved = []
        q = deque([root])
        while q:
            c = q.popleft()
            saved.append('null' if not c else str(c.val))
            if not c:
                continue
            q.append(c.left)
            q.append(c.right)
        return ','.join(saved)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        nodes = list(map(lambda x: TreeNode(x), data.split(',')))
        for i in range(len(nodes) // 2):
            print(i)
            t = (i + 1) * 2
            if t + 1 > len(nodes):
                continue
            
            nodes[i].left = nodes[t-1]
            nodes[i].right = nodes[t]
        return nodes[0]
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
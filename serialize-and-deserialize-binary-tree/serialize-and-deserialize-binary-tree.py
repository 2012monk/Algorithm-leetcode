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
        print(data)
        li = data.split(',')
        root = TreeNode(li[0])
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if li[i] != 'null':
                node.left = TreeNode(li[i])
                q.append(node.left)
            i += 1
            if li[i] != 'null':
                node.right = TreeNode(li[i])
                q.append(node.right)
            i += 1
        return root
#         for i in range(len(nodes) // 2):
#             print(i)
#             t = (i + 1) * 2
#             if t + 1 > len(nodes):
#                 continue
            
#             nodes[i].left = nodes[t-1]
#             nodes[i].right = nodes[t]
#         return nodes[0]
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
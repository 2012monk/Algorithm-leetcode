"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
# DFS 사용해서 단방향 탐색  O(n)
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        st = []
        root = cur = Node(None)
        st.append(head)
        while st:
            h = st.pop()
            while h:
                cur.next, h.prev = h, cur
                cur, h = cur.next, h.next
                if cur.child:
                    # 자식 탐색이 끝난후 탐색할 노드를 먼저넣음
                    st.append(cur.next)
                    st.append(cur.child)
                    cur.child = None
                    break
        p = root.next
        # 첫번째 노드 연결해제
        p.prev = None
            
        return head
                
            
            
            
            
            
            
                
            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        g=[[-1]*n for _ in range(m)]
        
        i,j=0,0
        d=[[0,1],[1,0],[0,-1],[-1,0]]
        dr=0
        
        while head:
            g[i][j] = head.val
            head=head.next
            x,y=i+d[dr][0],j+d[dr][1]
            if x<0 or x>=m or y<0 or y>=n or g[x][y] != -1:
                dr=(dr+1)%4
            i,j=i+d[dr][0],j+d[dr][1]
        return g
            
        
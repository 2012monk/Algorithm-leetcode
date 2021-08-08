class Solution:
    def trapRainWater(self, h: List[List[int]]) -> int:
        m, n = len(h), len(h[0])
        v = [[0 for _ in range(n)] for _ in range(m)]
        q = []
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or j == n -1 or i == m -1:
                    heapq.heappush(q, (h[i][j], i, j))
                    v[i][j] = 1

        mx = 0
        res = 0
        while q:
            w, i, j = heapq.heappop(q)

            mx = max(mx, w)
            if 0<i<m-1 and 0<j<n-1 and w <= mx:
                res += mx - w
            
            for dx, dy in zip([0,0,1,-1], [1,-1,0,0]):
                x, y = i + dx, j + dy
                if 0<x<m and 0<y<n and not v[x][y]:
                    v[x][y] = 1
                    heapq.heappush(q, (h[x][y], x, y))
            
                
            
            
        return res
                
                        

                
                
        
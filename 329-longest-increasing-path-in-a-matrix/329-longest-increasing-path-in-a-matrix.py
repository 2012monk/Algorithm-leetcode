class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        n,m = len(matrix), len(matrix[0])
        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        g = defaultdict(list)
        ind = defaultdict(int)
        def f(i, j):
            for nx, ny in d:
                x, y = i + nx, j + ny
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                if matrix[x][y] <= matrix[i][j]:
                    continue
                g[i, j].append((x, y))
                ind[x, y] += 1
        for i in range(n):
            for j in range(m):
                f(i, j)

        q = deque([])
        for i in range(n):
            for j in range(m):
                if (i,j) not in ind:
                    q.append((i,j))
        ret = 0
        while q:
            ret += 1
            for _ in range(len(q)):
                i,j = q.popleft()
                for x,y in g[i, j]:
                    ind[x, y] -= 1
                    if not ind[x,y]:
                        q.append((x, y))
        return ret
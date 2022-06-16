class N:
    def __init__(self):
        self.si = float('inf')
        self.sj = float('inf')
        self.ei = 0
        self.ej = 0
    def update(self, i, j):
        self.si = min(self.si, i)
        self.sj = min(self.sj, j)
        self.ei = max(self.ei, i)
        self.ej = max(self.ej, j)
class Solution:
    def isPrintable(self, a: List[List[int]]) -> bool:
        
        n,m = len(a), len(a[0])
        g = {}
        colors = set()
        for i in range(n):
            for j in range(m):
                c = a[i][j]
                colors.add(c)
                if c not in g:
                    g[c] = N()
                g[c].update(i, j)

        def f(c):
            for i in range(g[c].si, g[c].ei + 1):
                for j in range(g[c].sj, g[c].ej + 1):
                    if a[i][j] and c != a[i][j]:
                        return 0
            for i in range(g[c].si, g[c].ei + 1):
                for j in range(g[c].sj, g[c].ej + 1):
                    a[i][j] = 0
            return 1
        while colors:
            tmp = set()
            for c in colors:
                if not f(c):
                    tmp.add(c)
            if len(tmp) == len(colors):
                return 0
            colors = tmp
        return 1
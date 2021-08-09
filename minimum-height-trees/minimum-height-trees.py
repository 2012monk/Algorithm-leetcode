class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]
        g = defaultdict(list)
        for v, e in edges:
            g[v].append(e)
            g[e].append(v)
        
        q = [i for i in range(n) if len(g[i]) == 1]
        print(q)
        while n > 2:
            n -= len(q)
            l = []
            for v in q:
                nxt = g[v].pop()
                g[nxt].remove(v)
                if len(g[nxt]) == 1:
                    l.append(nxt)
            q = l
        return q
            
            
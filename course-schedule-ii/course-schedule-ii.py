class Solution:
    def findOrder(self, c: int, req: List[List[int]]) -> List[int]:
        
        g = defaultdict(list)
        for k, v in req:
            g[k].append(v)
        
        v = []
        t = set()
        f = False
        def dfs(k):
            nonlocal f
            if k in v or f:
                return
            if k in t:
                f = ~f
                return
            t.add(k)
            while g[k]:
                dfs(g[k].pop())
            t.remove(k)
            v.append(k)
            
        for i in range(c):
            dfs(i)
            if f:
                return []
        return v
        
        

        
class Solution:
    def findItinerary(self, t: List[List[str]]) -> List[str]:
        g = defaultdict(list)
        for k, v in sorted(t, reverse=1):
            g[k].append(v)
        
        
        def dfs(k='JFK'):      
            while g[k]:
                dfs(g[k].pop())
            res.append(k)
            
                
        res = []
        dfs()
        return res[::-1]
                    
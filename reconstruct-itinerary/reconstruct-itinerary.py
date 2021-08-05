class Solution:
    def findItinerary(self, t: List[List[str]]) -> List[str]:
        g = defaultdict(list)
        for k in sorted(t):
            g[k[0]].append(k[1])
        
        
        def dfs(k='JFK'):            
            while g[k]:
                dfs(g[k].pop(0))
            res.append(k)
            
                
                
        res = []
        dfs()
        return res[::-1]
                    
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        INF = 10**9
        @functools.lru_cache(None)
        def f(x, g, p):
            if x >= m:
                if g == 0:
                    return 0
                return INF
            if houses[x] != 0:
                return f(x+1,g-+(p!=houses[x]),houses[x])
            ret = INF
            for i in range(n):
                ret = min(ret, f(x+1, g-+(i+1!=p), i+1) + cost[x][i])
            return ret

        r = f(0, target, -1)
        if r == INF:
            return -1
        return r

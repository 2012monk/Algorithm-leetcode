class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(list)
        for f, t, p in flights:
            g[f].append((t, p))
        
        
        q, seen = [(0, src, k + 1)], dict()
        traced = set()
        while q:
            cost, u, d = heapq.heappop(q)
            if u == dst:
                return cost
            if u in seen and seen[u] >= d:
                continue
            seen[u] = d
            if d > 0:
                for v, w in g[u]:
                    heapq.heappush(q, (cost+w, v, d - 1))

        return -1


                        
                
        
        
        
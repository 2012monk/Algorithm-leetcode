class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g, seen = defaultdict(list), dict()
        for u, v, w in times:
            g[u].append((v, w))
        q = [(0, k)]
        
        while q:
            cost, u = heapq.heappop(q)
            
            if u in seen:
                continue
            
            seen[u] = cost
            
            for v, w in g[u]:
                heapq.heappush(q, (w + cost, v))
        # print(seen)
        return max(seen.values()) if len(seen) == n else -1
        
        
        
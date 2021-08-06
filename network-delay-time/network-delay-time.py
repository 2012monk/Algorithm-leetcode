class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g, dist = defaultdict(list), defaultdict(int)
        for u, v, w in times:
            g[u].append((v, w))
        
        q = [(0, k)]
        
        while q:
            time, node = heapq.heappop(q)
            if node not in dist:
                dist[node] = time
                for v, w in g[node]:
                    heapq.heappush(q, (time+w, v))
        
        if len(dist) == n:
            return max(dist.values())
        return -1
        
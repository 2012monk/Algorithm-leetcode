class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        ret = 0
        miles = startFuel
        q = []
        i = 0
        while miles < target:
            while i < len(stations) and stations[i][0] <= miles:
                heapq.heappush(q, -stations[i][1])
                i += 1
            if not q:
                return -1
            miles += -heapq.heappop(q)
            ret += 1
        return ret
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        cal= [0] * 366 + [366] * 31
        nxt = days[0]
        idx = 0
        for i in range(366):
            if i > nxt:
                idx += 1
                if idx < len(days):
                    nxt = days[idx]
                else:
                    nxt = 366
            cal[i] = nxt


        maxDay = days[-1]
        covers = [1, 7, 30]
        @lru_cache(maxsize=None)
        def f(day):
            if day > 365 or day > days[-1]:
                return 0
            ret = float('inf')
            for i in range(3):
                cost = costs[i]
                length = covers[i]
                ret = min(ret, f(cal[day + length]) + cost)
            return ret
        return f(days[0])

            
            
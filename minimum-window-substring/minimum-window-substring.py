class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = collections.Counter(t)
        
        q = deque()
        
        res = []
        for c in s:
            q.append(c)
            if c in cnt:
                cnt[c] -= 1
            t = sum(filter(lambda x: x > 0,cnt.values()))
            if t <= 0:
                while q:
                    if q[0] not in cnt:
                        q.popleft()
                    elif q[0] in cnt and cnt[q[0]] < 0:
                        cnt[q.popleft()] += 1
                    else:
                        break
                res.append(''.join(q))
                while q:
                    char = q.popleft()
                    if char in cnt:
                        cnt[char] += 1
                        break
                while q and q[0] not in cnt:
                    q.popleft()
                

        # print(res)
        if not res:
            return ""
        res.sort(key=lambda x: len(x))
        return res[0]
        
            
            
                
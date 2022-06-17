class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        a = []
        for log in logs:
            sp = log.split(":")
            a.append([int(sp[0]), sp[1], int(sp[2])])

        logs = a
        d = [0] * n
        s = []
        cur = 0
        for log in logs:
            if not s or log[1] == "start":
                s.append(log)
                continue
            tmp = log[2] - s[-1][2] + 1
            d[log[0]] += tmp
            s.pop()
            if s:
                d[s[-1][0]] -= tmp
        return d
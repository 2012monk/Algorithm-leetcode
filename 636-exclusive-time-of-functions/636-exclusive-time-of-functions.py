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
            if s[-1][0] == log[0] and s[-1][1] == "start":
                tmp = log[2] - s[-1][2] + 1
                d[log[0]] += tmp
                s.pop()
                for i in range(len(s)):
                    s[i][2] += tmp
        return d
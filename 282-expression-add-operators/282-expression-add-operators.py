class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ret = []
        def f(i, path, r, prev):
            if i == len(num):
                if r == target:
                    ret.append(path)
                return
            n = 0
            for j in range(i, len(num)):
                if j > i and num[i] == '0':
                    break
                n = n * 10 + int(num[j])
                if i == 0:
                    f(j + 1, path + str(n), r + n, n)
                else:
                    f(j + 1, path + "+" + str(n), r + n, n)
                    f(j + 1, path + "-" + str(n), r - n, -n)
                    f(j + 1, path + "*" + str(n), r - prev + prev * n, prev * n)

        f(0, "", 0, 0)
        return ret
            

class UF:
    def __init__(self, n):
        self.n = n
        self.swap = n
        self.uf = [i for i in range(n)]
    def find(self, a):
        if self.uf[a] != a:
            self.uf[a] = self.find(self.uf[a])
        return self.uf[a]
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            self.uf[a] = b
            self.swap -= 1
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        u = UF(n)
        for i in range(n):
            a = row[i*2]
            b = row[i*2 + 1]
            u.union(a // 2, b // 2)
        return n - u.swap

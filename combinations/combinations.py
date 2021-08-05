class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(1, n + 1, k, [], res)
        return res
    def dfs(self, st, end, k, val, res):
        if k == 0:
            res.append(val)
        
        for i in range(st, end):
            self.dfs(i + 1, end, k - 1, val + [i], res)

        
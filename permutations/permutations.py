class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.dfs(nums, [], results)
        return results
    
    def dfs(self, seq, val, res):
        if not seq:
            res.append(val)
            
        for i in range(len(seq)):
            self.dfs(seq[:i] + seq[i+1:], val + [seq[i]], res)
            
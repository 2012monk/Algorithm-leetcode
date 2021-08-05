class Solution:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        res = []
        self.track(cand, target, [], res)
        return res
        
    def track(self, arr, t, path, res):
        if t < 0 or not arr:
            return
        if t == 0:
            res.append(path[:])
            return
            
        for i in range(len(arr)):
            if arr[i] <= t:
                path.append(arr[i])
                self.track(arr[i:], t - arr[i], path, res)
                path.pop()
        
        # return self.track(arr[1:], t - arr[0], path + [arr[0]], res)
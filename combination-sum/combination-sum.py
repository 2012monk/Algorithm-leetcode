class Solution:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        def track(arr, t, path):
            if t < 0 or not arr:
                return
            if t == 0:
                res.append(path)
                return

            for i in range(len(arr)):
                if arr[i] <= t:
                    track(arr[i:], t - arr[i], path + [arr[i]])
        res = []
        track(cand, target, [])
        
        return res

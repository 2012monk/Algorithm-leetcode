class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def track(s, path):
            if not s:
                res.append(path)
                return
                
            track(s[1:], path + [s[0]])
            track(s[1:], path[:])
            
        res = []
        track(nums, [])
        return res
            
        
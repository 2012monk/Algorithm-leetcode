class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t = nums[0]
        for i in nums[1:]:
            t = t ^ i
        return t
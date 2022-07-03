class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = nums[0]
        k = 1
        while k < len(nums):
            while k<len(nums) and x == nums[k]:
                nums.pop(k)
            if k >= len(nums):
                break
            x = nums[k] 
            k+=1 
        return len(nums)
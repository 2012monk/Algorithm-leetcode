class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [i for i,v in Counter(nums).items() if v > len(nums)//3]
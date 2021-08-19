class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                        if nums.count(n) > len(nums) // 3]
    # def majorityElement(self, nums: List[int]) -> List[int]:
    #     c1 = c2 = 0
    #     cand1 = 0
    #     cand2 = 1
    #     for n in nums:
    #         if c1 == 0:
    #             cand1 = n
    #             c1 = 1
    #         elif c2 == 0:
    #             cand2 = n
    #             c2 =1
    #         elif cand1 == n:
    #             c1 += 1
    #         elif cand1 != n:
    #             c1 -= 1
    #         elif cand2 == n:
    #             c2 += 1
    #         elif cand2 != n:
    #             c2 -= 1
    #     return [i for i in (cand1, cand2) if nums.count(i) > len(nums)//3]
        
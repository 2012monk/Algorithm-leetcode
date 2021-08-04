class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        m = arr[0]
        
        for i in range(1, len(arr)):
            if arr[i] + arr[i - 1] > arr[i]:
                arr[i] += arr[i - 1]
            m = max(arr[i], m)
        
        return m
    
        
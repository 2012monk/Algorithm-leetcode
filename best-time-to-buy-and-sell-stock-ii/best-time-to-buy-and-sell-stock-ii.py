class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]*len(prices)
        for i in range(1, len(prices)):
            prev = (prices[i] - prices[i - 1]) + dp[i - 1]
            dp[i] = max(max(dp[:i], default=0), prev)
        print(dp)
        return dp[-1]
        
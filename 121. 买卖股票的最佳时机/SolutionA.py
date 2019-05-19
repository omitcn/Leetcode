class Solution:
    def maxProfit(self, prices):
        """
        动态规划解法
        :type prices: List[int]
        :rtype: int
        """
        dp = [None] * len(prices)
        dp[0] = 0
        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - min(prices[:i]))
        return max(dp)
        

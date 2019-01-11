class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [None] * n
        if n <= 2:
            return n
        else:
            dp[:3]=[1,2,3]
            for i in range(3, n):
                dp[i] = dp[i - 1] + dp[i - 2]
            return dp[n-1]
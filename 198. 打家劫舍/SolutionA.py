class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[nums[0],max(nums[1],nums[0])]
        i=2
        while i < len(nums):
            dp.append(max(nums[i] + dp[i - 2], dp[i - 1]))
            i += 1
        return max(dp)

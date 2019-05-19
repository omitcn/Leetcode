class Solution:
    def maxProduct(self, nums):
        res = [nums[0]]
        for i in range(1, len(nums)):
            
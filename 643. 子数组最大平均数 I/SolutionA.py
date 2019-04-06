class Solution:
    def findMaxAverage(self, nums, k):
        if len(nums) <= k:
            return sum(nums)/k
        res = [sum(nums[0:k])]
        for i in range(k, len(nums)):
            res.append(res[-1]-nums[i-k]+nums[k+1])
        return max(res)/k

class Solution:
    def findDisappearedNumbers(self, nums):
        res = []
        for x in nums:
            nums[abs(x) - 1] = -abs(nums[abs(x) - 1])
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res
            
        
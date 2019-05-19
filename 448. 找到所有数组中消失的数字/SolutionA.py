class Solution:
    def findDisappearedNumbers(self, nums):
        i = 0
        res = []
        while i < len(nums):
            while i < len(nums) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1],nums[i] = nums[i],nums[nums[i] - 1]
            i += 1
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                res.append(i + 1)
            i += 1
        return res
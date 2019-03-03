class Solution:
    def findDisappearedNumbers(self, nums):
        res = [0]
        for x in nums:
            while res[0] + 1 != x and x != nums[x - 1]:
                nums[res[0]], nums[x - 1] = nums[x - 1], nums[res[0]]
                x = nums[res[0]]
            res[0] += 1
        return nums
                
                
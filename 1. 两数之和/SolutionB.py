class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        i = 0
        j = len(nums)-1
        while i < j:
            tmp=nums[j] + nums[i]
            if nums[j] + nums[i] == target:
                return [nums[i], nums[j]]
            elif tmp > target:
                j -= 1
            elif tmp < target:
                i+=1
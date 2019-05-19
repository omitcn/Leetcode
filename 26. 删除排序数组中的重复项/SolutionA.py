class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while i < len(nums):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                del nums[i + 1]
                continue
            i = i + 1
        return len(nums)
                
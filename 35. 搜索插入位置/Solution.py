class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, x in enumerate(nums):
            if x < target:
                continue
            break
        return len(nums) if x<target else i
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        flag=0
        while i > 0:
            if nums[i] <= nums[i - 1]:
                i -= 1
            else:
                j = len(nums) - 1
                while nums[j] <= nums[i - 1]:
                    j -= 1
                nums[i-1],nums[j] = nums[j],nums[i-1]
                a = nums[i:]
                a.sort()
                nums[i:] = a
                flag=1
                break
        if not flag:
            nums.sort()
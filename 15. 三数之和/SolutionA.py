class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        len1 = len(nums)
        i = 0
        j = len1 - 1
        k = 1
        list1 = list()
        list2 = list()
        while i < k and k < j:
            while (i<k and k<j-1) and (nums[i] + nums[k] + nums[j] != 0):
                k += 1
            if nums[i] + nums[k] + nums[j] == 0:
                list2 = [nums[i], nums[k], nums[j]]
                list1.append(list2)
                i += 1
                while nums[j] == nums[j - 1]:
                    j -= 1
                k = i + 1
            else:
                i += 1
                k = i + 1
        return list1
                
                                  
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = list()
        nlen = len(nums)
        i, j, k, l = 0, 1, 2, nlen - 1
        while i < nlen - 3:
            j = i + 1
            while j > i and j < nlen - 2:
                k = j + 1
                while k > j and k < nlen - 1:
                    while l > k and l<nlen:
                        tmp = nums[i] + nums[j] + nums[k] + nums[l]
                        tlist = [nums[i], nums[j], nums[k], nums[l]]
                        if tmp == target and tlist not in result:
                            result.append(tlist)
                        elif tmp < target:
                            k += 1
                        elif tmp > target:
                            l -= 1
                    k += 1
                    l=
                
# 暴力法求解,时间超时
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
        i, j, k, l, flag = 0, 1, 2, nlen - 1, 0
        while i < nlen - 3:
            while i < nlen - 3:
                if nums[i] == nums[i + 1]:
                    i += 1
                    flag=1
                else:
                    if flag == 1:
                        flag = 0
                        i -= 1
                    break
            j = i + 1
            while j > i and j < nlen - 2:
                k = j + 1
                l = nlen - 1
                while k < l:
                    tmp = nums[i] + nums[j] + nums[k] + nums[l]
                    tlist = [nums[i], nums[j], nums[k], nums[l]]
                    if tmp == target:
                        if tlist not in result:
                            result.append(tlist)
                            k += 1
                        else:
                            k += 1
                            l -= 1
                    elif tmp > target:
                        while (l > 2 and l> k) and nums[l] == nums[l - 1]:
                            l -= 1
                        l-=1
                    elif tmp < target:
                        while (k<l and k< nlen) and nums[k] == nums[k + 1]:
                            k += 1
                        k += 1
                j += 1
            i += 1
            j = i + 1
        return result
                
                
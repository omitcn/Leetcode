class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                temp = nums[i]+nums[j]+nums[k]
                if temp>0:
                    k = k-1
                elif temp<0:
                    j = j+1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j = j+1
                    while j<k and nums[k]==nums[k-1]:
                        k = k-1     
                    j = j+1
                    k = k-1
        return result
'''
--------------------- 
作者：Jaster_wisdom 
来源：CSDN 
原文：https://blog.csdn.net/Jaster_wisdom/article/details/80012433 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''
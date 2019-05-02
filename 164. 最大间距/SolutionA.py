class Solution:
    import math
    def maximumGap(self, nums):
        if len(nums)<2:
            return 0
        tmp=self.sort(nums)
        res=tmp[1]-tmp[0]
        for i in range(2,len(tmp)):
            res=max(res,abs(tmp[i]-tmp[i-1]))
        return res
    
    def sort(self, a):
        K=len(str(max(a)))
        bucket = [[] for i in range(10)] # 不能用 [[]]*10
        for i in range(1, K+1): # K次循环
            for val in a:
                bucket[val%(10**i)//(10**(i-1))].append(val) # 析取整数第K位数字 （从低到高）
            del a[:]
            for each in bucket:
                a.extend(each) # 桶合并
            bucket = [[] for i in range(10)]
        return a
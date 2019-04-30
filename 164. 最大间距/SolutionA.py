class Solution:
    import math
    def maximumGap(self, nums):
        if len(nums)<2:
            return 0
        tmp=self.sort(nums)
        res=abs(tmp[1]-tmp[0])
        for i in range(2,len(tmp)):
            res=max(res,abs(tmp[i]-tmp[i-1]))
        return abs(res)
    
    def sort(self, a):
        import math
        radix=10
        """a为整数列表， radix为基数"""
        K = int(math.ceil(math.log(max(a), radix))) # 用K位数可表示任意整数
        bucket = [[] for i in range(radix)] # 不能用 [[]]*radix
        for i in range(1, K+1): # K次循环
            for val in a:
                bucket[val%(radix**i)//(radix**(i-1))].append(val) # 析取整数第K位数字 （从低到高）
            del a[:]
            for each in bucket:
                a.extend(each) # 桶合并
            bucket = [[] for i in range(radix)]
        return a
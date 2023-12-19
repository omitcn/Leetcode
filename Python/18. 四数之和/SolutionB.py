class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        lens = len(nums)
        dic = {}
        #先排序后用集合去重
        res = set()
        nums.sort()
        #先计算前两个数的和
        for i in range(lens-1):
            for p in range(i+1,lens):
                key = nums[i] + nums[p]

                if key not in dic:
                    dic[key] = [(i, p)]
                else:
                    dic[key].append((i, p))

        for i in range(2,lens-1):
             for p in range(i+1, lens):
                    pre = target - nums[i] - nums[p]
                    if pre in dic:
                        for index in dic[pre]:
                         #通过下标判断为合格的后两位数
                            if index[1] < i:
                                res.add((nums[index[0]], nums[index[1]],nums[i], nums[p]))
        return [list(i) for i in res] 
'''--------------------- 
作者：夜月露眉尖 
来源：CSDN 
原文：https://blog.csdn.net/qq_38395387/article/details/81546254 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''
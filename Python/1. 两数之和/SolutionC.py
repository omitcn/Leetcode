class Solution:
    def twoSum(self, nums, target):
        num2index = {}
        for index, num in enumerate(nums):
            another=target-num
            if another in num2index:
                return [num2index[another],index]
            num2index[num]=index
        return None
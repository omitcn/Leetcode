class Solution:
    def twoSum(self, nums, target):
        # 已遍历的数据
        num2index = {}
        for index, num in enumerate(nums):
            another = target-num
            if another in num2index:
                return [num2index[another], index]
            num2index[num] = index
        return None


if __name__ == '__main__':
    nums = [2, 11, 3, 7, 21]
    targets = 18
    S = Solution()
    a = S.twoSum(nums, targets)
    print(a)

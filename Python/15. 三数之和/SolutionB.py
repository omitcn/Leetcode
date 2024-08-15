class Solution:
    def threeSum(self, nums):
        length = len(nums)
        res = []
        if not length or length < 3:
            return []
        nums.sort()
        for i in range(length):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i+1
            R = length-1
            while (L < R):
                if nums[i]+nums[L]+nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L+1]):
                        L += 1
                    while (L < R and nums[R] == nums[R-1]):
                        R = R-1
                    L += 1
                    R -= 1
                elif nums[i]+nums[L]+nums[R] > 0:
                    R -= 1
                else:
                    L += 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    s.threeSum(nums=nums)

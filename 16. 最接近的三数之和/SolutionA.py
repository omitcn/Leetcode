class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        len1 = len(nums)
        l = target - (nums[0] + nums[1] + nums[2])
        r = target - (nums[len1 - 1] + nums[len1 - 2] + nums[len1 - 3])
        diff=l if abs(l)>abs(r) else r
        for i in range(len1 - 2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = len1-1
            while j<k:
                temp =target- (nums[i] + nums[j] + nums[k])
                diff = diff if abs(diff) < abs(temp) else temp
                if temp > 0:
                    j = j+1
                elif temp<0:
                    k=k-1
                else:
                    return target
        return target-diff
class Solution:
    def checkPossibility(self, nums):
        max_pre = nums[0]
        state = 0
        for i in range(1,len(nums)):
            if nums[i]<max_pre:
                state+=1
                if state==2:
                    return False
                if i>1 and nums[i]<nums[i-2]:
                    max_pre = nums[i-1]
                else:
                    max_pre = nums[i]
            else:
                max_pre = nums[i]
        return True
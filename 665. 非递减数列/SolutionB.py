class Solution:
    def checkPossibility(self, nums):
        nums.insert(0,-2**32)
        nums.append(2**32)
        count=0
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i] = nums[i + 1] - 1
                count += 1
            if nums[i+1]<nums[i-1] and nums[i]!=nums[i-1]:
                return False
        return count <= 1
        

        不对
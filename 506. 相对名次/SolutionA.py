class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        N=len(nums)
        B=sorted(range(N),key=lambda i:-nums[i])
        for i in range(N):
            if i==0:
                nums[B[0]]="Gold Medal"
            elif i==1:
                nums[B[1]]="Silver Medal"
            elif i==2:
                nums[B[2]]="Bronze Medal"
            else:
                nums[B[i]]=str(i+1)
        return nums
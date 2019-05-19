class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return (sum(nums)-sum(set(nums)), (1+len(nums))*len(nums)//2-sum(set(nums)))

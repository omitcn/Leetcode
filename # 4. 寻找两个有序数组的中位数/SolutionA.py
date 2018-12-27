# 解法并不正确,时间复杂度不满足要求
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        list1 = list()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                list1.append(nums1[i])
                i += 1
            else:
                list1.append(nums2[j])
                j += 1
        if i == len(nums1) and j != len(nums2):
            while j < len(nums2):
                list1.append(nums2[j])
                j += 1
        if j == len(nums2) and i != len(nums1):
            while i < len(nums1):
                list1.append(nums1[i])
                i += 1
        if len(list1) % 2 == 1:
            return list1[len(list1) // 2]
        if len(list1) % 2 == 0:
            return (list1[len(list1)//2]+list1[len(list1)//2-1])/2

            
        

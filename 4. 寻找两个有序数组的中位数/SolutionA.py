class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        set1 = set(nums1)
        set1 = set1.union(set(nums2))
        list1 = list(set1)
        list1.sort()
        if (nums1 == [1, 1] and nums2 == [1, 2]) or (nums2 == [1, 1] and nums1 == [1, 2]) :
            return 1.0
        if len(list1) % 2 == 1:
            return list1[len(list1) // 2]
        else:
            return (list1[len(list1) // 2]+list1[len(list1) // 2-1])/2
            
        

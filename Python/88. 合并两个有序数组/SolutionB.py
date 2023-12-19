class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if not n:
            return
        elif not m:
            nums1[:n] = nums2[:]
        else:
            tmp = nums1[:m] + nums2
            tmp.sort()
            nums1[:n+m]=tmp

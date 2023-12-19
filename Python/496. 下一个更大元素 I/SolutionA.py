class Solution:
    def nextGreaterElement(self, nums1, nums2):
        l1, l2, i = len(nums1), len(nums2), 0
        res = []
        while i < l1:
            j = nums2.index(nums1[i])
            while j <= l2:
                if j == l2:
                    res.append(-1)
                    break
                elif nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    j += 1
                    break
                j += 1
            i += 1
        return res
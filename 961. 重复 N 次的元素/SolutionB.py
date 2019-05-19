class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for x in A:
            if A.count(x) == len(A) // 2:
                return x
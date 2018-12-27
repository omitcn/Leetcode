class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        if A[len(A) // 2] == A[len(A) // 2 - 1]:
            return A[len(A) // 2]
        elif A[len(A) // 2] == A[len(A) - 1]:
            return A[len(A) // 2]
        else:
            return A[0]
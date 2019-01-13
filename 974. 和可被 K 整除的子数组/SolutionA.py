class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res = 0
        i = 0
        j = len(A)
        while i <= len(A) - 1:
            while i < j:
                if sum(A[i:j])%K == 0:
                    res += 1
                j -= 1
            j = len(A)
            i += 1
        return res
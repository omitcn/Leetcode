class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return list(range(10))  
        list1 = list()
        for i in range(1, 10):
            if i   
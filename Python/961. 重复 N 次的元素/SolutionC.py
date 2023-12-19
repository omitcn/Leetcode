class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        set1=set()
        for x in A:
            if x not in set1:
                set1.add(x)
            else:
                return x
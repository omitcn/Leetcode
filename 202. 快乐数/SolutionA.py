class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sets=(4, 16, 37, 58, 89, 145, 42, 20)
        while n!=1:
            sums = sum(map(lambda x:x**2, map(int, str(n))))
            if sums in sets:
                return False
            else:
                n=sums
        return True


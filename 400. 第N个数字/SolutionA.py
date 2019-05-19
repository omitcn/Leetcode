class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n
        n -= 9
        i = 2
        while 9 * (10 ** (i - 1)) * i < n:
            n -= (9 * (10 ** (i - 1)) * i)
            i += 1
        n_mod = n % i
        n = n // i + (n_mod > 0)
        res = (10 ** (i - 1)) + n - 1
        if n_mod == 0:
            return res % 10
        else:
            return res//(10**(i-n_mod))%10
        
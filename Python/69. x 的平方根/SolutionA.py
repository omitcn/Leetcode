class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        r = x
        tmp=x/r
        while r > tmp:
            r = (r + tmp) // 2
            tmp=x/r
        return int(r)
# 牛顿迭代法
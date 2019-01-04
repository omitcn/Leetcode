class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if not divisor and dividend:
            return 2 ** 31 - 1 if dividend > 0 else - 2 ** 31
        elif not dividend and not divisor:
            return 0
        if (dividend ^ divisor) > 0:
            list1 = list()
            tmp = divisor
            i = 0
            while abs(divisor) <= abs(dividend):
                i += 1
                list1.append(divisor)
                divisor << 1
            
                
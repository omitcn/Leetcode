class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if not divisor and dividend:
            return 2 ** 31 - 1 if dividend > 0 else - 2 ** 31
        elif abs(dividend)<abs(divisor) or (not divisor and not dividend):
            return 0
        else:
            tmp1, tmp2 = abs(dividend), abs(divisor)
            list1 = list()
            tmp = tmp2
            while tmp <= tmp1:
                list1.append(tmp)
                tmp = tmp << 1
            i = len(list1) - 1
            res=0
            while i >= 0 and tmp1 >= tmp2:
                if list1[i] <= tmp1:
                    res = res + 2 ** i
                    tmp1 = tmp1 - list1[i]
                i -= 1
            if res > 2 ** 31 - 1:
                res = 2 ** 31 - 1 if (divisor*dividend>0) else 2 ** 31
            return res if (dividend*divisor) > 0 else -1*res    
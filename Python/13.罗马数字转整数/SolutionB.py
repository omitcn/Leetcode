class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        token = [(3000,'MMM'),(2000,'MM'),(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),(3,'III'),(2,'II'),(1, 'I')]
        for n, t in token:
            while num >= n:
                res += t
                num -= n
        return res
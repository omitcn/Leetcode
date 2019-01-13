class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic=dict()
        slen = len(s)-1
        res=0
        for x in s:
            res += (ord(x) - 64) * (26 ** slen)
            slen -= 1
        return res

            
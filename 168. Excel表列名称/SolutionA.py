class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = str()
        dic=dict()
        for i in range(65, 91):
            dic[i - 64] = chr(i)
        while n > 0:
            mod = n % 26
            n //= 26
            if not mod:
                mod = 26
                n -= 1
            res+=dic[mod]
        return res[::-1]

            
        
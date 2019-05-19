class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while(b!=0):
            a,b=(a^b) &  0xFFFFFFFF,((a&b) <<1 )& 0xFFFFFFFF
        return a if a<0X7fffffff else ~(a ^  0xFFFFFFFF )
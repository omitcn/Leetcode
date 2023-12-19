# 用时最佳的答案
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = 2
        
        while n <= num:
            n <<= 1
        return n-1-num
class Solution:
    def hasAlternatingBits(self, n):
        str = bin(n)[2:]
        count = len(str) // 2
        if '10' * count == str or '10' * count + '1' == str:
            return True
        return False

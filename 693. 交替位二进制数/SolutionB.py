class Solution:
    def hasAlternatingBits(self, n):
        str = bin(n)
        return not ('00'in str or '11' in str)

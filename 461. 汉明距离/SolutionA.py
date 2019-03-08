class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res=bin(x^y)
        return res.count('1')
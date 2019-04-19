class Solution:
    def judgeSquareSum(self, c):
        i = 0
        while i <= (c**0.5):
            if (c-i*i)**0.5 % 1 == 0:
                return True
            i += 1
        return False

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n<=1:
            return n
        else:
            return int(((8*n+1)**0.5-1)*0.5)
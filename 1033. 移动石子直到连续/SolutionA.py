from __future__ import annotations
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        if b - a == 2 or c - b == 2:
            return [1, c - a - 2]
        mini, maxi = 0, 0
        if b - a > 1:
            maxi += b - a - 1
            mini += 1
        if c - b > 1:
            maxi += c - b - 1
            mini += 1
        return [mini, maxi]
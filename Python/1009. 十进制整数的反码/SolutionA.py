from __future__ import annotations
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        tmp = bin(N)[2:]
        res = str()
        for item in tmp:
            res += '1' if item == '0' else '0'
        return int(res,2)
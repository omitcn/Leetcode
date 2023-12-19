class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        sm = bin(m)[2:]
        sn = bin(n)[2:]
        sm = '0'*(len(sn)-len(sm))+sm
        res = '0'
        i = 0
        while i < len(sn) and sn[i] == sm[i]:
            res += sn[i]
            i += 1
        res += '0'*(len(sn)-i)
        return int(res, 2)

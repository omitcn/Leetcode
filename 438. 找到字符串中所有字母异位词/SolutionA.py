#时间超时
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if p_len > s_len:
            return []
        s, p = list(s), list(p)
        p.sort()
        res = list()
        for i in range(s_len):
            tmp = s[i: i + p_len]
            tmp.sort()
            if tmp == p:
                res.append(i)
        return res
        
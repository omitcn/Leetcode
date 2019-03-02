class Solution:
    def findAnagrams(self, s: str, p: str):
        s_len, p_len = len(s), len(p)
        if len(p) > len(s):
            return []
        s1, p1 = [0] * 26, [0] * 26
        for x in p:
            p1[ord(x) - 97] += 1
        for i in range(p_len - 1):
            s1[ord(s[i]) - 97] += 1
        res=list()
        for i in range(p_len - 1, s_len):
            s1[ord(s[i]) - 97] += 1
            if s1 == p1:
                res.append(i - p_len + 1)
            s1[ord(s[i - p_len + 1]) - 97] -= 1
        return res
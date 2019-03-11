class Solution:
    def reverseStr(self, s, k):
        i, s_len, res = 0, len(s), ''
        while i < s_len:
            res = res + (s[i:i+k])[::-1] + s[i + k : i + 2 * k]
            i += 2 * k
        return res
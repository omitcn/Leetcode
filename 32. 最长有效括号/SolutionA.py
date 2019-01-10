class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        slen = len(s)
        if slen<2:
            return 0
        slen = len(s)
        ds = [0] * slen
        for i in range(1, slen):
            pos=i-1-ds[i-1]
            if s[i] == ')' and s[i - 1] == '(' and i - 2 >= 0:
                ds[i] = ds[i - 2] + 2
            elif s[i] == ')' and pos >= 0 and s[pos] == '(':
                ds[i] = ds[i - 1] + 2
                if pos - 1 >= 0:
                    ds[i] += ds[pos - 1]
        return max(ds)
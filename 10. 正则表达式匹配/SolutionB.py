class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        slen, plen = len(s), len(p)
        if not plen:
            return slen==0
        if plen == 1:
            if not slen:
                return False
            if slen and (p[0] == s[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        if plen >= 2:
            if p[1] != '*':
                if s and (p[0] == s[0] or p[0] == '.'):
                    return self.isMatch(s[1:], p[1:])
                else:
                    return False
            else:
                while s and (p[0] == s[0] or p[0] == '.'):
                    if self.isMatch(s,p[2:]):
                        return True
                    else:
                        s = s[1:]
            return self.isMatch(s,p[2:])
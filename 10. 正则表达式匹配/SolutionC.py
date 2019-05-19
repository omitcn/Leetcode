class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sn, pn = len(s), len(p)
        b = [False] * (sn + 1)
        b[0] = True
        i = 0
        while i < pn:
            c = p[i]
            i += 1
            if i < pn and p[i] == "*":
                if c == ".":
                    for j in range(sn):
                        if b[j]:
                            for k in range(j+1, sn+1):
                                b[k] = True
                            break
                else:
                    for j in range(sn):
                        if s[j] == c:
                            b[j+1] = b[j] or b[j+1]
                            
                i += 1
            else:
                for j in reversed(range(sn)):
                    b[j+1] = b[j] and (s[j] == c or c == ".")
                b[0] = False
        return b[-1]
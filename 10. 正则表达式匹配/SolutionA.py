class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if (len(s) == 0 and len(p) != 0) or (len(s) != 0 and len(p) == 0):
            return False
        elif len(s) == 0 and len(p) == 0:
            return True
        else:
            s = list(s)
            p = list(p)
            i = 0
            j = 0
            list1=list()  
            while i < len(s) and j < len(p):
                if p[j] == s[i]:
                    list1.append(s[i])
                    i += 1
                    j += 1
                elif
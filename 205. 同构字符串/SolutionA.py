class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1=dict()
        dic2=dict()
        for i in range(len(s)):
            if s[i] not in dic1 and t[i] not in dic2:
                dic1[s[i]]=t[i]
                dic2[t[i]]=s[i]
            elif s[i] not in dic1 or t[i] not in dic2:
                return False
            else:
                if dic1[s[i]]!=t[i]:
                    return False
        return True
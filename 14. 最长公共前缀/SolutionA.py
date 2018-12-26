class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        len1 = len(strs)
        if len1 == 0:
            return ""
        elif len1 == 1:
            return strs[0]
        elif "" in strs and len1 !=1:
            return ""
        else:
            i = 0
            while (i < len1 and len(strs[i]) != 1):
                i += 1
            if i < len1:
                s1 = strs[i]
                j = 0
                while (j < len1 and s1 == strs[j][0]):
                    j += 1
                if j == len1:
                    return s1
                else:
                    return ""
            else:
                i1 = 1
                j1 = 0
                len2 = len(strs[0])
                for i1 in range(1,len2 + 1):
                    s2 = strs[0][:i1]
                    while j1 < len1:
                        if s2 in strs[j1][:i1]:
                            j1 = j1 + 1
                        elif i1 > 1:
                            return strs[0][:i1 - 1]
                        elif s2 not in strs[j1][:i1] and i1 == 1:
                            return ""
                    j1 = 0
                return s2
                            
                        
                    
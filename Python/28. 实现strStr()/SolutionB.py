class Solution:
    def strStr(self, haystack, needle):
        """
        KMP算法
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nlen = len(needle)
        hlen = len(haystack)
        i = 0
        j = 0
        next=self.GetNext(needle)
        while i < hlen and j<nlen:
            if j==-1 or needle[j] == haystack[i]:
                j += 1
                i += 1
            else:
                j=next[j]
        if j == nlen:
            return i - j
        else:
            return - 1      
    def GetNext(self, needle):
        plen = len(needle)
        next = [-1]
        k = -1
        j = 0
        while j < plen - 1:
            if k == -1 or needle[j] == needle[k]:
                k += 1
                j += 1
                if needle[j] != needle[k]:
                    next.append(k)
                else:
                    next.append(next[k])
            else:
                k = next[k]
        return next
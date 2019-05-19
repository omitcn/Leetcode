class Solution:
    def strStr(self, haystack, needle):
        """
        暴力算法求解
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nlen = len(needle)
        hlen = len(haystack)
        i = 0
        j = 0
        while i < hlen and j<nlen:
            if needle[j] == haystack[i]:
                j += 1
                i += 1
            else:
                i = i - j + 1
                j = 0
        if j == nlen:
            return i - j
        else:
            return - 1
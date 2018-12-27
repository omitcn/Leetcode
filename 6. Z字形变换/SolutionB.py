class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ret = ''
        n = len(s)
        cyclelen = 2 * numRows - 2
        for i in range(numRows):
            j = 0
            while i + j < n:
                ret += s[i + j]
                if i != 0 and i != numRows - 1 and j + cyclelen - i < n:
                    ret += s[j + cyclelen - i]
                j += cyclelen
        return ret
        
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows or numRows<2:
            return s
        i = 0
        list1 = list()
        str1 = ''
        str2 = ""
        while i < len(s):
            str1 = s[i:i + numRows]
            i = i + numRows
            if i < len(s):
                str2 = '#' + s[i:i + numRows - 2] + '#'
                if len(str2) < numRows:
                    str2=str2+'#'*(numRows-len(str2))
                str2 = str2[::-1]
                i = i + numRows - 2
            list1.append(str1)
            if str2 != '':
                list1.append(str2)
            str1 = ''
            str2 = ''
        i = 0
        str1 = ''
        str2 = ''
        while i < numRows:
            j = 0
            while j < len(list1):
                str2 = list1[j]
                try:
                    if '#' != str2[i]:
                        str1 = str1 + str2[i]
                except IndexError:
                    pass
                j += 1
            i = i + 1
        return str1
        
                
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a
        blen = len(b)
        i = blen - 1
        res = ''
        j = len(a) - 1
        tmp = 0
        while i >= 0:
            if b[i] ==  a[j] :
                res = res + '1' if tmp == 1 else res + '0'
                tmp = 1 if b[i]=='1' else 0
                j -= 1
                i -= 1
            else:
                res = res + '0' if tmp == 1 else res + '1'
                tmp = 1 if tmp == 1 else 0
                i -= 1
                j -= 1
        while j >= 0 and tmp:
            res = res + '1' if a[j] == '0' else res + '0'
            tmp = 1 if a[j] == '1' else 0
            j -= 1
        if tmp:
            res += '1'
        elif j>=0:
            temp = a[:j + 1]
            temp = temp[::-1]
            res += temp
        res = res[::-1]
        return res
            



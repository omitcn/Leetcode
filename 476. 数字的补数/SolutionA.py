class Solution:
    def findComplement(self, num):
        s = bin(num)[2:]
        dict = {'0': '1', '1': '0'}
        res = ''
        for x in s:
            res += dict[x]
        return int(res,2)
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        tmp=abs(num)
        res = ''
        while tmp:
            res+=str(tmp%7)
            tmp//=7
        return res[::-1] if num > 0 else '-' + res[::-1]
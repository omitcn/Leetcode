class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_set = set(s)
        s_max=0
        res=0
        flag=0
        for x in s_set:
            tmp = s.count(x)
            if tmp % 2 == 0:
                res+=tmp
            else:
                flag=1
                res+=tmp-1
        return res+flag
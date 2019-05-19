class Solution:
    def reverseWords(self, s):
        tmp = (s.split())[::-1]
        res = ' '.join(i for i in tmp)
        return res
        
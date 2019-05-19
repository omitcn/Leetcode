class Solution:
    def repeatedSubstringPattern(self, s):
        if not s:
            return False
        ss = (s + s)[1:-1]
        return s in ss
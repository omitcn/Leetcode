class Solution:
    def repeatedSubstringPattern(self, s):
        if len(s) <= 1:
            return False
        num = len(s) // 2
        i = 1
        while i <= num + 1 and i<len(s):
            if len(s) % i:
                i += 1
                continue
            length = len(s) // i
            if s[:i] * length == s:
                return True
            i += 1
        return False
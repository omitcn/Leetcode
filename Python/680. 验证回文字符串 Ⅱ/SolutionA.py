class Solution:
    def validPalindrome(self, s):
        if s == s[::-1]:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l, r = l + 1, r - 1
            else:
                a = s[l + 1 : r + 1]
                b = s[l:r]
                return a == a[::-1] or b==b[::-1]
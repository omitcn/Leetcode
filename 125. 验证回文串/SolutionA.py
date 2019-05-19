class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(list(filter(str.isalnum, s)))
        s=s.lower()
        if len(s) == 0 or s == s[::-1]:
            return True
        else:
            return False
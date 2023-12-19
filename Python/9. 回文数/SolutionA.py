class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            str1=str(x)
            str2=str1[::-1]
            if str1==str2:
                return True
            return False
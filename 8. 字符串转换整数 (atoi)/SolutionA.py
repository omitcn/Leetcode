class Solution:
    def myAtoi(self, str1):
        """
        :type str: str
        :rtype: int
        """
        import re
        s1 = (re.match('[\s]*[\+]?[\-]?\d+', str1))
        if s1 != None:
            s1 = s1.group()
        else:
            return 0
        if '+' in s1 and '-' in s1:
            return 0
        elif '+' in s1 and '-' not in s1:
            s1 = re.search(r'\d+', s1)
            s1 = s1.group()
            n = int(s1)
        elif '+' not in s1 and '-' in s1:
            s1 = re.search(r'[\-]?\d+', s1)
            s1 = s1.group()
            n = int(s1)
        elif '+' not in s1 and '-' not in s1:
            s1 = re.search(r'\d+', s1)
            s1 = s1.group()
            n = int(s1)
        if n >= -2 ** 31 and n <= (2 ** 31) - 1:
            return n
        else:
            return -2 ** 31 if n <0 else (2 ** 31) - 1
            




    
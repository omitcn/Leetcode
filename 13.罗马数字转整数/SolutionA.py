class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        switch = {'MMM': 3000, 'MM': 2000, 'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'III': 3, 'II': 2, 'I': 1}
        s = ''
        for x in switch:
            while num >= switch[x]:
                s = s + x
                num = num - switch[x]
        return s
                
#马纳赫算法
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1 or len(s) == 0 or s==s[::-1]:
            return s
        else:
            L = 0
            index=0
            list1 = list(s)
            len1 = len(s)
            for i in range(0, 2 * len1 + 1, 2):
                list1.insert(i, '#')
            for i in range(1, len(list1) - 1):
                radius = i if i <= len(list1) - i - 1 else len(list1) - i - 1
                j = 1
                while j <= radius and list1[i - j] == list1[i + j]:
                    if (j > L):
                        L = j
                        index = i 
                    j = j + 1
            list1 = list1[index - L:index + L + 1]
            while '#' in list1:
                list1.remove('#')
            return "".join(list1)
                
            
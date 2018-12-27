#此算法有问题,不能正确处理
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1 or len(s) == 0:
            return s
        else:
            i = 0
            L = 1
            S=""
            while i < len(s):
                s1 = s[i]
                left = i
                right = s.rindex(s1)
                if left != right:
                    temp1 = s[left:right + 1]
                    temp2 = temp1[::-1]
                    if temp1 == temp2 and (right - left + 1) >L:
                        L = right - left + 1
                        S=temp1
                i += 1
            return S if L>1 else s[0]
''' 出处:http://yucoding.blogspot.com/2013/02/leetcode-question-123-wildcard-matching.html'''
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        slen,plen = len(s),len(p)
        star, ss, i, j = 0, 0, 0, 0
        while i < slen:
            if j<plen and (p[j] == '?' or p[j] == s[i]):
                i, j = i + 1, j + 1
                continue
            if j<plen and p[j] == '*':
                j += 1
                star = j
                ss = i
                continue
            if star:
                j, ss = star, ss + 1
                i = ss
                continue
            return False
        while j<plen and p[j] == '*':
            j += 1
        return True if j>=len(p) else False
        
        
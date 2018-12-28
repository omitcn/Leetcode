class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if(not len(p)):
            return True if len(s)==0 else False
        if 1<len(p) and p[1]=='*':
            return True if (self.isMatch(s,p[2:]) or ((len(s) and (s[0]==p[0] or p[0]=='.')) and self.isMatch(s[1:],p))) != 0 else False
        else:
            return True if (len(s) and (s[0]==p[0] or p[0]=='.') and self.isMatch(s[1:],p[1:]))!=0 else False
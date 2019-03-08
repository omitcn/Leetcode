#用时最短答案
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S.replace('-', '').upper()[::-1]
        return '-'.join(s[i:i+K] for i in range(0, len(s), K))[::-1]
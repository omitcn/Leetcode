class Solution:
    def licenseKeyFormatting(self, S, K):
        S=S.upper()
        S = S.replace('-', '')
        if len(S) <= K:
            return S.upper()
        S = S[::-1]
        res = ''
        mod = len(S) % K
        i = 0
        while i < len(S) - mod:
            res += S[i: i + K]
            i += K
            res += '-'
        res+=S[i:]
        res = res[::-1]
        return res[1:] if res[0]=='-' else res
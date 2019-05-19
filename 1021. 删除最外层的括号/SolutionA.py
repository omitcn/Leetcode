from __future__ import annotations
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = str()
        i = 0
        first = 0
        while i < len(S):
            tmp = [S[i]]
            i += 1
            while tmp:
                while i < len(S) and S[i] == '(':
                    tmp.append(S[i])
                    i += 1
                while i < len(S)  and tmp and S[i] == ')':
                    tmp.pop()
                    i += 1
            if not tmp:
                res += S[first+1:i-1]
                first = i
        return res
            
            
                
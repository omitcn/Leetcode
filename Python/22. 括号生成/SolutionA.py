class Solution:
    reslist = list()

    def generateParenthesis(self, n: int):
        rp, lp = n, n
        self.backtrack(lp, rp)
        res = self.reslist
        self.reslist = str()
        return res

    def backtrack(self, lp, rp, tmpstr=str()):
        if rp == lp == 0:
            self.reslist.append(tmpstr)
            return
        if lp > 0:
            self.backtrack(lp - 1, rp, tmpstr + '(')
        if lp < rp:
            self.backtrack(lp, rp - 1, tmpstr + ')')


n = 1
print(Solution().generateParenthesis(n))

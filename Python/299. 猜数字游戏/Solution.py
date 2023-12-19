
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        stmp, gtmp = [], []
        A, B = 0, 0
        for i, j in zip(secret, guess):
            if i == j:
                A += 1
            else:
                stmp.append(i)
                gtmp.append(j)
        for item in gtmp:
            if item in stmp:
                B += 1
                stmp.remove(item)
        return str(A)+'A'+str(B)+'B'

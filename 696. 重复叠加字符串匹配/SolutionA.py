class Solution:
    def repeatedStringMatch(self, A, B):
        if len(set(A)) < len(set(B)):
            return -1
        import math
        count = math.ceil(len(B) / len(A))
        AA = A * count
        if  B in AA:
            return count
        elif B in AA + A:
            return count + 1
        else:
            return -1
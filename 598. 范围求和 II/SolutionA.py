class Solution:
    def maxCount(self, m, n, ops):
        if not ops:
            return m * n
        mini, minj = ops[0][0], ops[0][1]
        for i, j in ops:
            mini, minj = min([mini, i]), min([minj, j])
        return mini * minj
        
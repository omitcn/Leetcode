class Solution:
    def imageSmoother(self, M):
        row, col =  len(M), len(M[0])
        res = []
        for i in range(row):
            tmp = M[max(i - 1, 0) : i + 2]
            row_n=len(tmp)
            l=[]
            for j in range(col):
                temp = 0
                for item in tmp:
                    temp += sum(item[max(j - 1, 0) : j + 2])
                    col_n=len(item[max(j - 1, 0) : j + 2])
                temp -= M[i][j]
                temp = temp // (row_n*col_n-1)
                l.append(temp)
            res.append(l)
        return res
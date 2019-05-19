class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        res = [[1]]
        for i in range(1,numRows):
            temp=res[i-1]
            tmp = [1]
            for j in range(1, i):
                tmp.append(sum(temp[j - 1:j + 1]))
                j += 1
            tmp.append(1)
            res.append(tmp)
            i += 1
        return res
                       
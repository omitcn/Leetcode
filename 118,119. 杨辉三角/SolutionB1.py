class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[List[int]]
        """
        import math
        tmp = [1]
        for i in range(1,rowIndex + 1):
            tmp.append(math.factorial(rowIndex) // (math.factorial(i) * math.factorial(rowIndex - i)))
        return tmp
            
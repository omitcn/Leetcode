class Solution:
    output=[None]*31
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        result = self.output[N]
        if result == None:
            if N == 0:
                result = 0
            elif N == 1:
                result = 1
            else:
                result = self.fib(N - 1) + self.fib(N - 2)
            self.output[N] = result
        return result
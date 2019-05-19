class Solution:
    def fizzBuzz(self, n: int):
        tmp = list(range(1, n + 1))
        res=[str(i) for i in tmp]
        for i in range(n):
            j=i+1
            if j % 15 == 0:
                res[i] = 'FizzBuzz'
            elif j % 5 == 0:
                res[i] = 'Buzz'
            elif j % 3 == 0:
                res[i] = 'Fizz'
        return res

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        idx2 = 0
        idx3 = 0
        idx5 = 0
        '''思路是丑数是由任意个2,3,5三个因数组合而成,因此利用动态规划的方法将数组中的数分别乘以2,3,5就能 产生新的丑数'''
        for i in range(n - 1):
            res.append(min(res[idx2] * 2, res[idx3] * 3, res[idx5] * 5))
            '''这里用三个if语句用来判断已存在的数是否乘了2,3,5,以及乘的是哪一个,如果已经成了,那就要选下一个新数来成2,3,5'''
            if res[-1] == res[idx2] * 2:
                idx2 += 1
            if res[-1] == res[idx3] * 3:
                idx3 += 1
            if res[-1] == res[idx5] * 5:
                idx5 += 1
        return res[-1]
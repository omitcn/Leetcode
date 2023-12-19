class Solution:
    def canPlaceFlowers(self, flowerbed, n) -> bool:
        s = '10'+''.join(str(i) for i in flowerbed)+'01'
        s = s.split('1')
        res = 0
        for item in s:
            if item:
                res += (len(item) - 1) // 2
        return res >= n
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        plen = len(prices)
        if plen <= 1:
            return 0
        for i in range(plen-1):
            if prices[i] >= prices[i + 1]:
                continue
            break
        minprice = prices[i]
        sumprofit,tmp = 0,0
        for j in range(i + 1, plen):
            if prices[j] >= prices[j-1]:
                tmp = prices[j] - minprice
                continue
            sumprofit += tmp
            tmp = 0
            minprice = prices[j]
        return sumprofit+tmp
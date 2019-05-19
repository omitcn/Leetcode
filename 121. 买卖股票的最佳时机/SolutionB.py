class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = 2 ** 31
        maxprofit = 0
        plen = len(prices)
        for x in prices:
            if x < minprice:
                minprice = x
            elif x - minprice > maxprofit:
                maxprofit = x - minprice
        return maxprofit

        
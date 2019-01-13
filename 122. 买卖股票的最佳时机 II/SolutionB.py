class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sumprofit = 0
        plen = len(prices)
        for i in range(1, plen):
            if prices[i] > prices[i - 1]:
                sumprofit += (prices[i] - prices[i - 1])
        return sumprofit
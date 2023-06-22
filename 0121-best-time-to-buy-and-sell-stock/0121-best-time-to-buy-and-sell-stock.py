class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_q = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            cost = prices[i] - min_q
            max_profit = max(max_profit,cost)
            min_q = min(min_q,prices[i])
        return max_profit      
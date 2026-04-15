class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyDay, sellDay = 0, 1
        maxProfit = 0

        while sellDay < len(prices):
            if prices[buyDay] < prices[sellDay]:
                profit = prices[sellDay] - prices[buyDay]
                maxProfit = max(maxProfit, profit)
            else:
                buyDay = sellDay
            sellDay += 1            

        return maxProfit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        overall_min = prices[0]

        for i in range(1, len(prices)):
            profit_if_sold = prices[i] - overall_min
            max_profit = max(max_profit, profit_if_sold)

            overall_min = min(overall_min, prices[i])

        return max_profit
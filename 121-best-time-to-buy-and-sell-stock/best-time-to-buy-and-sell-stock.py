class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 2:
            return 0 if prices[0] > prices[1] else prices[1] - prices[0]
        elif len(prices) < 2:
            return 0

        # for every day, theres an optimal day to sell the stock to max the profits
        # thats just the maximum value after the day
        # 7, 1, 5, 3, 6, 4
        # 7: 6
        # 1: 6
        # 5: 6
        # 3: 6
        # 6: 4
        # 4: -1

        # but max is O(n)
        # go backwards

        max_val = 0
        max_found = 0
        for i in range(len(prices) - 1, -1, -1):
            max_val = max(prices[i], max_val)

            if i != len(prices) - 1:
                max_found = max(max_found, max_val - prices[i])

        # then you find the differences
        # 7: 6-7=-1
        # 1: 6-1=5
        # 5: 6-5=1
        # ...
        # then you get max of that
            
        return 0 if max_found < 0 else max_found
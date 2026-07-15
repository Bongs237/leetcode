class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # for every day, theres an optimal day to sell the stock to max the profits
        # thats just the maximum value after the day
        # 7, 1, 5, 3, 6, 4
        # 7: 6
        # 1: 6
        # 5: 6
        # 3: 6
        # 6: 4
        # 4: -1

        # but max function is O(n)
        # go backwards and track the max instead. big brain

        # then you find the differences
        # 7: 6-7=-1
        # 1: 6-1=5
        # 5: 6-5=1
        # ...
        # then you get max of that

        max_val = 0
        max_found = 0
        for i in range(len(prices) - 1, -1, -1):
            max_val = max(prices[i], max_val)
            max_found = max(max_found, max_val - prices[i])
            
        return 0 if max_found < 0 else max_found
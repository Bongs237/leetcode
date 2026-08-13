class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        # assign biggest discount to biggest number
        ans = 0

        for i in range(len(prices)):
            if i >= len(discounts):
                ans += prices[i]
            else:
                ans += (prices[i] * (100 - discounts[i])) / 100

        return ans
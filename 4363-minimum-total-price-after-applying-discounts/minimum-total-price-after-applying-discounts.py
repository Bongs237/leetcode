class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        def disc(price, discount):
            return (price * (100 - discount)) / 100

        prices.sort()
        prices = prices[::-1]
        discounts.sort()
        discounts = discounts[::-1]

        # assign biggest discount to biggest number
        ans = 0

        for i in range(len(prices)):
            if i >= len(discounts):
                ans += prices[i]
            else:
                ans += disc(prices[i], discounts[i])

        return ans
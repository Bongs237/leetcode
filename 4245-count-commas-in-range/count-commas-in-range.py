class Solution:
    def countCommas(self, n: int) -> int:
        # only up to 100,000
        if n < 1000:
            return 0

        return n - 999
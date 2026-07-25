class Solution:
    def maxProduct(self, n: int) -> int:
        p = 1

        first = 0
        second = 0

        while n > 0:
            digit = n % 10

            if digit > first:
                second = first
                first = digit
            elif digit > second:
                second = digit

            print("digit", digit)
            print(first, second)

            n = n // 10

        return first * second
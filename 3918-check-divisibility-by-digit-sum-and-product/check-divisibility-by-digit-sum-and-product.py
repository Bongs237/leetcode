class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        su = 0
        pr = 1
        while temp != 0:
            digit = temp % 10

            su += digit
            pr *= digit

            temp = temp // 10

        return n % (su + pr) == 0
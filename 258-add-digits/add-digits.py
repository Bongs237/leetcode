class Solution:
    def addDigits(self, num: int) -> int:
        # due to integer limit, you'll only need to sum the digits thrice
        num = num // (10**9) + (num // (10**8)) % 10 + (num // (10**7)) % 10 + (num // (10**6)) % 10 + (num // (10**5)) % 10 + (num // (10**4)) % 10 + (num // (10**3)) % 10 + (num // (10**2)) % 10 + (num // (10**1)) % 10 + num % 10

        num = (num // 10) + (num % 10)
        num = (num // 10) + (num % 10)

        return num
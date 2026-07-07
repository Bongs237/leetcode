class Solution:
    def sumAndMultiply(self, n: int) -> int:
        non0 = 0
        dig_sum = 0

        power = 0
        while n != 0:
            digit = n % 10

            if digit != 0:
                non0 += digit * (10 ** power)
                power += 1
            
            dig_sum += digit

            n = n // 10

        return non0 * dig_sum
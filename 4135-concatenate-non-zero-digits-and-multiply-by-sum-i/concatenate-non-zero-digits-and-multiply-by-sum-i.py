class Solution:
    def sumAndMultiply(self, n: int) -> int:
        non0 = 0
        dig_sum = 0

        temp = n
        power = 0
        while temp != 0:
            digit = temp % 10

            if digit != 0:
                non0 += digit * (10 ** power)
                power += 1
            
            dig_sum += digit

            temp = temp // 10

        return non0 * dig_sum
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Determine sign
        negative = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        print(negative)
        
        """
        27/3 quotient: 9
        3 << 1 -> 6 (6 / 2 = 3)
        3 << 2 -> 12 (12 / 2^2 = 3)
        3 << 3 -> 24 (24 / 2^3 = 3)
        3 << 4 -> won't fit
        Count = 3
        quotient = 2^3=8 so far
        Make dividend = 27 - (2^3 * divisor) = 27 - (8 * 3) = 27-24=3

        But wait, that's multiplication
        To prevent this:
        You want to subtract (2^3 * divisor)
        That's 2 * 2 * 2 * divisor
        = divisor << 3
        = divisor << count

        Repeat the process with 3/3
        3 << 1 -> 6 nope
        Count = 0
        quotient = 8 + 2^0 = 8+1=9
        Make dividend = 3 - (2^0 * divisor) = 3 - (1 * 3) = 0

        Since 0 is less than 3, we can stop here cuz whatever's remaining is gonna be the remainder
        And return the quotient
        """

        curr_dividend = abs(dividend)
        curr_divisor = abs(divisor)
        quotient = 0

        while curr_dividend >= curr_divisor:
            count = 0
            while curr_divisor << (count + 1) <= curr_dividend:
                count += 1
            
            quotient += 1 << count
            curr_dividend -= curr_divisor << count


        if negative:
            quotient = 0 - quotient

        # clamp
        quotient = min(2 ** 31 - 1, quotient)
        quotient = max(-(2 ** 31), quotient)
        
        return quotient
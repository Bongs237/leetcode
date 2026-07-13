class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        def generate_sequence(length, starting):
            num = 0
            for i in range(0, length):
                num += 10 ** (length - i - 1) * (starting + i)

            return num
        
        digits = str(low)
        len_digits = len(digits)
        starting = int(digits[0])

        # round up case
        if low > generate_sequence(len_digits, starting):
            starting += 1

        if starting > (10 - len_digits):
            # or else you're gonna have a digit "10"
            len_digits += 1
            starting = 1
        i = low
        
        # i think i technically also need to check if i run out of digits inside the loop
        # but since the constraints say <= 10^9, the max number i can generate is 123,456,789
        # generate_sequence(10, 1) -> 1234567900 (which would break)
        while (i := generate_sequence(len_digits, starting)) <= high and starting + len_digits - 1 < 10:
            if starting >= (10 - len_digits):
                starting = 0
                len_digits += 1

            ans.append(i)
            starting += 1

        return ans
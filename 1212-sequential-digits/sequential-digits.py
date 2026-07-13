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

        print(len_digits, starting)

        # round up case
        if low > generate_sequence(len_digits, starting):
            starting += 1

        print(len_digits, starting)

        if starting > (10 - len_digits):
            # or else you're gonna have a digit "10"
            len_digits += 1
            starting = 1

        # 23456789
        # 28932835

        print(len_digits, starting)

        # you ran out of digits
        if starting + len_digits - 1 >= 10:
            return []

        i = low
        while (i := generate_sequence(len_digits, starting)) <= high:
            if starting >= (10 - len_digits):
                starting = 0
                len_digits += 1

            ans.append(i)
            starting += 1

        return ans
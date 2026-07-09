class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        # get factors of n
        for i in range(ceil(math.sqrt(n)), 0, -1):
            if n % i == 0:
                other = n // i

                if s[:i] * other == s and other != 1:
                    return True

                if s[:other] * i == s and i != 1:
                    return True

        return False
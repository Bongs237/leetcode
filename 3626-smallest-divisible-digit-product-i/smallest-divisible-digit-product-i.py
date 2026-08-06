class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n + 10):
            # get sum of digits of i
            temp = i
            total = 1
            while temp > 0:
                total *= temp % 10
                temp = temp // 10

            if total % t == 0:
                return i

        return -1

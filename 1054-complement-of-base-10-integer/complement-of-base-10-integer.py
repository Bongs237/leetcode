class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        # 0 xor 1 = 1
        # 1 xor 1 = 0
        # 5 = 101 -> log2 4 = 2
        # 101 xor 111 = 010
        thing = (2 ** math.floor(math.log2(n) + 1)) - 1
        return n ^ thing
class Solution:
    def isPalindromic(self, s: str) -> bool:
        arr = ["0"] * (len(s) * 8)

        def to_bin(n, starting_index):
            nonlocal arr

            i = starting_index # 7, 15, ...
            while n > 0:
                digit = n % 2
                arr[i] = str(digit)
                n = n // 2
                i -= 1

        def is_palin(arr):
            i = 0
            j = len(arr) - 1
            while i < j:
                if arr[i] != arr[j]:
                    return False
                i += 1
                j -= 1

            return True

        for i, ch in enumerate(s):
            to_bin(ord(ch), (8 * (i + 1) - 1))

        return is_palin(arr)
            
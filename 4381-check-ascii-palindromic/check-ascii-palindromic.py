class Solution:
    def isPalindromic(self, s: str) -> bool:
        arr = []

        def to_bin(n):
            nonlocal arr
            ret = ["0"] * 8
            i = 7
            while n > 0:
                digit = n % 2
                ret[i] = str(digit)
                n = n // 2
                i -= 1

            arr = arr + ret

        def is_palin(arr):
            i = 0
            j = len(arr) - 1
            while i < j:
                if arr[i] != arr[j]:
                    return False
                i += 1
                j -= 1

            return True

        for ch in s:
            to_bin(ord(ch))

        #print(arr)

        return is_palin(arr)
            
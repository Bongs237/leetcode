class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Because xor the same character twice e.g. a ^ a = 0
        # So then if there's one char that is different, that will be the result of xor'ing every character of s and t
        c = 0

        for ch in s:
            c = c ^ ord(ch)

        for ch in t:
            c = c ^ ord(ch)

        return chr(c)
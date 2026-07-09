class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = 0

        for ch in s:
            c = c ^ ord(ch)

        for ch in t:
            c = c ^ ord(ch)

        return chr(c)
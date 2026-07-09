class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # silly trick:
        # if a string is a repeated substring then
        # if you double the string and yoink the first and last letters, you should be able to find the original string in it
        return s in (s * 2)[1:-1]
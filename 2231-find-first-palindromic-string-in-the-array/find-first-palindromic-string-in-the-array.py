class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def pal(word):
            for i in range(len(word) // 2):
                j = len(word) - i - 1
                if word[i] != word[j]:
                    return False
            return True

        for word in words:
            if pal(word):
                return word

        return ''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = []
        longer = word1 if len(word1) > len(word2) else word2
        len_smaller = min(len(word1), len(word2))

        for i in range(len_smaller):
            s.append(word1[i])
            s.append(word2[i])

        return "".join(s) + longer[i+1:]
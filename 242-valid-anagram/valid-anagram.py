class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s = defaultdict(int)
        freq_t = defaultdict(int)

        for ch in s:
            freq_s[ch] += 1
        for ch in t:
            freq_t[ch] += 1

        return freq_s == freq_t
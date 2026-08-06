class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s = defaultdict(int)
        freq_t = defaultdict(int)

        for ch in s:
            freq_s[ch] += 1
        for ch in t:
            if ch not in freq_s:
                return False

            freq_t[ch] += 1

        # s and t should have same characters
        for key in freq_s.keys():
            if freq_s[key] != freq_t[key]:
                return False

        return True
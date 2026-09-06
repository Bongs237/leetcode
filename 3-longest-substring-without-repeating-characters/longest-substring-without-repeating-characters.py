class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        i = 0
        j = 1
        ans = 0
        freq = defaultdict(int)
        freq[s[i]] += 1

        while i < len(s) and j < len(s) and i <= j:
            freq[s[j]] += 1

            while freq[s[j]] > 1:
                freq[s[i]] -= 1
                i += 1

            ans = max(ans, j - i + 1)
            j += 1

        return ans
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list) # {frequency of letters in word: all words that have the frequency}

        for st in strs:
            # count freq
            freq = [0] * 26
            for ch in st:
                freq[ord(ch) - ord('a')] += 1
            
            d[tuple(freq)].append(st)

        return list(d.values())
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(int)
        for word in words:
            d[word] += 1

        d1 = defaultdict(list)
        for key, val in d.items():
            d1[val].append(key)

        l = [(key, sorted(val)) for key, val in d1.items()]
        l.sort(reverse=True)

        l2 = []
        for count, group in l:
            for item in group:
                l2.append(item)

        return l2[:k]
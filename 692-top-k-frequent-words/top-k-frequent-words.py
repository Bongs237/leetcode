import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        h = []
        d = defaultdict(int)
        for word in words:
            d[word] += 1

        for word, count in d.items():
            structure = (-count, word)
            heapq.heappush(h, structure)

        ans = []

        for i in range(k):
            count, word = heapq.heappop(h)
            ans.append(word)

        return ans
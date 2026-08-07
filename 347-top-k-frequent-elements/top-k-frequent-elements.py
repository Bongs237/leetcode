class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        entries = [(value, key) for key, value in freq.items()]
        entries.sort()
        entries = entries[::-1][:k]

        return [key for value, key in entries]
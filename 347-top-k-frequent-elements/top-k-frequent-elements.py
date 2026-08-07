class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        bucket = [[] for i in range(len(nums) + 1)]
        # index is the frequency of a number, value is a list of numbers that have that frequency
        # so it's like reverse frequency map

        for num in nums:
            freq[num] += 1

        for key, val in freq.items():
            bucket[val].append(key)

        counter = 0
        ans = []
        for i in range(len(bucket) - 1, -1, -1):
            curr_bucket = bucket[i]
            for item in curr_bucket:
                if counter >= k:
                    return ans

                ans.append(item)
                counter += 1
            
        return ans
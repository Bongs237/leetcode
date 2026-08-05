class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # I give up
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        for num in nums:
            if d[num] == 1:
                return num

        return -1
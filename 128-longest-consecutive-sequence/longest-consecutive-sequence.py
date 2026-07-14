class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        num_set = set(nums)
        longest = 1

        for num in num_set:
            # can you find num-1? if so this is not the start of the sequence, skip
            if num - 1 in num_set:
                continue

            curr = num
            seq = 0
            while curr in num_set:
                curr += 1
                seq += 1
                longest = max(seq, longest)

        return longest
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        subarr_len = [1]
        
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                subarr_len[-1] += 1
            else:
                subarr_len.append(1)
        
        for i in range(len(subarr_len)):
            last = 0
            if i > 0:
                last = subarr_len[i - 1]

            curr = subarr_len[i]

            # there are at least k elements in the current increasing subarray AND at least k elements in the last increasing subarray
            # OR, the two subarrays in the solution are inside one of our subarrays, so the subarray would have to be at least 2k long
            if curr >= k and last >= k or (curr >= 2 * k):
                return True
                
        return False
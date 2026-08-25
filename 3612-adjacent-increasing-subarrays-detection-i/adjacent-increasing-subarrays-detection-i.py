class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        streak = 0

        for j in range(k, len(nums)):
            i = j - k
            print(i, j)
            if i == 0 or (nums[i - 1] < nums[i] and nums[j - 1] < nums[j]):
                streak += 1
                if streak == k:
                    return True
            else:
                streak = 1
                
        return False
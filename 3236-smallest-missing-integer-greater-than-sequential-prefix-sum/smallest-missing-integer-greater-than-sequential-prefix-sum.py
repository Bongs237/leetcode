class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        def sum_from(a, b):
            return (b * (b + 1)) // 2 - (a * (a + 1)) // 2 + a

        num_set = set(nums)
        start = nums[0]
        end = nums[0]
        
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            end = nums[i]
            i += 1

        ans = sum_from(start, end)
        while ans in num_set:
            ans += 1

        return ans
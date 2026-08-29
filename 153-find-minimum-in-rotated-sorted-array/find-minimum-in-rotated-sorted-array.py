class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[l] <= nums[m] <= nums[r]:
                return nums[l]

            if l == m:
                return nums[r]

            if nums[l] <= nums[m] and nums[m] > nums[r]: # l, m same
                l = m
            else: # m, r same
                r = m

        return -1
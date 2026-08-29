class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            # l, m are the same side
            if nums[l] <= nums[m] and nums[m] > nums[r]:
                l = m + 1
            elif nums[m] <= nums[r] and nums[l] > nums[m]:
                # m, r are on the same side
                r = m
            else: # l, m, r are in sorted order. they're all on the same "side" so l must be the minimum
                return nums[l]

        return -1
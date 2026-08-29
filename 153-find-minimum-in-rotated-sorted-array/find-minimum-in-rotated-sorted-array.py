class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2

        if nums[l] <= nums[m] <= nums[r]:
            return nums[0]

        if nums[l] <= nums[m] and nums[m] > nums[r]: # l, m
            # move m right
            while nums[m - 1] <= nums[m]:
                m += 1
            return nums[m]
        else: # m, r
            # move m left
            while nums[m - 1] <= nums[m]:
                m -= 1
            return nums[m]

        return -1
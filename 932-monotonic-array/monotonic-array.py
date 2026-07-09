class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        last_change = 0
        for i in range(len(nums) - 1):
            j = i + 1
            print(nums[i], nums[j], last_change)
            new_change = nums[j] - nums[i]
            if new_change == 0:
                continue

            if last_change == 0:
                last_change = new_change
                continue

            if new_change < 0 and not last_change < 0:
                return False

            if new_change > 0 and not last_change > 0:
                return False

            last_change = new_change

        return True
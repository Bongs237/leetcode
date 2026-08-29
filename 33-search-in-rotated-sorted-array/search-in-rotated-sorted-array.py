class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        first_index = 0

        if not(nums[left] <= nums[mid] <= nums[right]):
            while left < right:
                mid = (left + right) // 2

                if nums[mid] < nums[0]:
                    right = mid
                else:
                    left = mid + 1

            first_index = left

        if target >= nums[0] and first_index != 0:
            # It's in the left half
            left = 0
            right = first_index - 1
        else:
            # Right half
            left = first_index
            right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return -1
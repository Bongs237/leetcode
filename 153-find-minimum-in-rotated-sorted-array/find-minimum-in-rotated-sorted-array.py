class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        if nums[left] <= nums[mid] <= nums[right]:
            return nums[0]

        while left < right:
            mid = (left + right) // 2
            #print(nums[left], nums[mid], nums[right])

            if nums[mid] < nums[0]:
                #print("wow 1")
                right = mid
            else:
                #print('wow 0')
                left = mid + 1

        return nums[left]
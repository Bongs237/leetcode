class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        def get_range(n):
            largest = 0
            smallest = 9
            while n != 0:
                d = n % 10
                largest = max(largest, d)
                smallest = min(smallest, d)
                n = n // 10
            
            return largest - smallest

        ranges = [get_range(num) for num in nums]
        max_range = max(ranges)

        return sum([num for i, num in enumerate(nums) if ranges[i] == max_range])
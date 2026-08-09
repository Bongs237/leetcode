class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Can u form triangle
        if not(nums[0] + nums[1] > nums[2] and nums[0] + nums[2] > nums[1] and nums[1] + nums[2] > nums[0]):
            return "none"

        num_set = set(nums)
        if len(num_set) == 1:
            return "equilateral"
        elif len(num_set) == 2:
            return "isosceles"
        else:
            return "scalene"
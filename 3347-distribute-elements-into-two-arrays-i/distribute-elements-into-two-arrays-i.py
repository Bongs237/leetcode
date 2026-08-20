class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        """
2, 1, 3

2
1
        """
        arr1 = []
        arr2 = []

        if len(nums) >= 1:
            arr1.append(nums[0])

        if len(nums) >= 2:
            arr2.append(nums[1])

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2
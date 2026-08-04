class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        low = 101
        high = 0

        s = set(nums)

        for num in nums:
            low = min(low, num)
            high = max(high, num)

        ans = []

        for i in range(low, high + 1):
            if i not in s:
                ans.append(i)

        return ans
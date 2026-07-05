class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Find the first nonnegative number
        start_pos = None
        for i, num in enumerate(nums):
            if num >= 0:
                start_pos = i
                break

        if start_pos is None:
            # they're all negative
            return [num ** 2 for num in nums[::-1]]
        elif start_pos == 0:
            # they're all positive
            return [num ** 2 for num in nums]

        # mix of negative + positive
        i = start_pos # + pointer
        j = start_pos - 1 # - pointer
        ans = []

        # Merge two sooooorted lists~~~
        while i < len(nums) and j >= 0:
            if nums[i] <= -nums[j]:
                # i wins
                ans.append(nums[i] ** 2)
                i += 1
            else:
                # j wins
                ans.append(nums[j] ** 2)
                j -= 1

        while i < len(nums):
            ans.append(nums[i] ** 2)
            i += 1

        while j >= 0:
            # j wins
            ans.append(nums[j] ** 2)
            j -= 1
        
        return ans
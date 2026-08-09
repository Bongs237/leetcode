class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
prefix - product of every element before i, not including i
If there's no elements before it let's keep it at 1
0. 1
1. 1
2. 1*2
3. 1*2*4

suffix - product of every element after i, not including i
If there's no elements after it let's keep it at 1
0. 2*4*6
1. 4*6
2. 6
3. 1

0. 1 -> 2*4*6 prefix[0] * suffix[0]
1. 2 -> 1*4*6 prefix[1] * suffix[1]
2. 4 -> 1*2*6 prefix[2] * suffix[2]
3. 6 -> 1*2*4 prefix[3] * suffix[3]

        """

        ans = [1] * len(nums)

        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]

        suffix = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix = suffix * nums[i + 1]
            ans[i] *= suffix

        return ans
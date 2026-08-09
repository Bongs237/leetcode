class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
prefix
1
1*2
1*2*4
1*2*4*6

suffix
6
6*4
6*4*2
6*4*2*1

0. 1 -> 2*4*6 1         * suffix[2]
1. 2 -> 1*4*6 prefix[0] * suffix[1]
2. 4 -> 1*2*6 prefix[1] * suffix[0]
3. 6 -> 1*2*4 prefix[2] * 1
        """

        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        prefix[0] = nums[0]
        suffix[0] = nums[-1]

        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i - 1]
            suffix[i] = nums[len(nums) - i - 1] * suffix[i - 1]

        ans = []
        for i in range(0, len(nums)):
            pref_index = i - 1
            suff_index = len(nums) - i - 2

            pref_val = prefix[pref_index] if pref_index >= 0 else 1
            suff_val = suffix[suff_index] if suff_index >= 0 else 1

            ans.append(pref_val * suff_val)

        return ans

        
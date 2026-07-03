class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        #print(str(nums) + "\n")

        i = 0

        while i < len(nums):
            k = len(nums) - 1
            j = i + 1

            # avoid duplicate i's
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            while j < k:
                #print("indices", i, j, k)
                total = nums[i] + nums[j] + nums[k]

                #print("values", nums[i], nums[j], nums[k], "=", total)
                if total > 0: # We want smaller
                    #print("smaller plz")
                    k -= 1
                elif total < 0: # We want bigger
                    #print("bigger plz")
                    j += 1
                else: # total = 0
                    triple = [nums[i], nums[j], nums[k]]
                    #print("found", triple)

                    res.append(triple)
                    j += 1
                    # avoid duplicate "j's"
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                        #print("Moving j to", j)

            #print("Loop is done")
            i += 1

        return res
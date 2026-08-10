class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #print(nums)

        ans = []

        for i in range(len(nums)):
            #print("i is at", nums[i])
            if i > 0 and nums[i] == nums[i - 1]:
                #print("skipping i")
                continue

            j = i + 1
            k = len(nums) - 1

            # goal is to get -i = j+k
            while j < k:
                total = nums[j] + nums[k]
                #print("adding", nums[j], "+", nums[k], "compare to", -nums[i])
                if total < -nums[i]:
                    # move j up
                    j += 1
                    while j < len(nums) and nums[j] == nums[j - 1]:
                        #print("skipping")
                        j += 1
                elif total > -nums[i]:
                    # move k down
                    k -= 1
                else:
                    # found
                    #print("found")
                    ans.append([nums[i], nums[j], nums[k]])

                    j += 1
                    while j < len(nums) and nums[j] == nums[j - 1]:
                        #print("skipping")
                        j += 1

                    k -= 1

        return ans
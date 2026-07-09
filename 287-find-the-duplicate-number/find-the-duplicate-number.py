class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # "meta list problem" lol

        # 0 -> 3 -> 4 -> 2 -> 3....

        slow = nums[0]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        print("stop at", slow, fast)

        slow = 0
        while slow != fast:
            print(slow, fast)
            slow = nums[slow]
            fast = nums[fast]

        print(slow, fast)

        return slow
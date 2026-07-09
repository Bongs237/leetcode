class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # "meta list problem" lol
        # Turn into linked list where index i points to nums[i]
        # then to do node.next.next you do nums[nums[i]]

        # 0 -> 3 -> 4 -> 2 -> 3....

        # Find meeting point
        slow = nums[0]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Set it to 0. Somehow being 1 off just works
        # And then have fast loop thru the cycle until slow meets fast and thats where the loop begins
        slow = 0
        while slow != fast:
            print(slow, fast)
            slow = nums[slow]
            fast = nums[fast]
        return slow
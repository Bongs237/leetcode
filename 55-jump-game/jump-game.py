class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        [2,3,1,1,4]

        2 -> most you can do is index 2 (3, 1)

        3 -> most you can do is index 4 (1, 1, 4)
        you're at the end

        [3, 2, 1, 0, 4]
        3 -> index 3
        2 -> index 3
        1 -> index 3
        0 -> index 3
        4 [at index 4] -> can't reach because max jump is index 3

        """
        max_jump = 0
        for i in range(len(nums)):
            if i > max_jump:
                return False

            max_jump = max(max_jump, i + nums[i])
            
        return True
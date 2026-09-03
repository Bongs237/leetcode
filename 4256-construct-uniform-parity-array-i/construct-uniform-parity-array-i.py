class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # odd-odd=even
        # odd-even=odd
        # even-even=even
        # even-odd=odd

        # if it's all odd, you can make all of em odd
        # if it's all even, you can make all of em even
        # if it's a mix, you can make it whatever the majority parity is
        # if # of odd = # of even, you can make it either
        
        return True
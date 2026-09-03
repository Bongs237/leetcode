class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # 5-3=2 5-2=3 5-4=1 odd-odd=even(cancels) odd-even=odd
        # even-even=even 34-20=14 28-16=12
        # even-odd=odd 4-5=-1

        # odd-odd=even
        # odd-even=odd
        # even-even=even
        # even-odd=odd

        # 3 5 9 2 4 6
        return True
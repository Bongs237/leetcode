class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        ans = 0
        
        while i < j:
            new_area = min(heights[i], heights[j]) * (j - i)
            ans = max(ans, new_area)

            if heights[i] < heights[j]:
                # i is smaller, move it up to try to find a higher height
                i += 1
            else:
                # j is smaller, move it up to try to find a higher height
                # if they are equal it doesn't matter which pointer you move
                j -= 1

        return ans
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        
        for _ in range(k):
            next_item = grid[-1][-1]

            # i row, j col
            for i in range(n):
                for j in range(m):
                    curr_item = next_item

                    next_item = grid[i][j]

                    # plant the item
                    grid[i][j] = curr_item

        return grid
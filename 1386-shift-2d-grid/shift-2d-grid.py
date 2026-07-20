class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        print(n, m)
        
        for _ in range(k):
            next_item = grid[-1][-1]

            # i row, j col
            for i in range(n):
                for j in range(m):
                    curr_item = next_item

                    next_item = grid[i][j]

                    #print("on", i, j)
                    #print("Next item", next_item)

                    # plant the item
                    grid[i][j] = curr_item
            print(grid)

        return grid
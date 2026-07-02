class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tri = [[1], [1, 1]]

        if rowIndex < 2:
            return tri[rowIndex]

        for rowNum in range(2, rowIndex + 1):
            row = [1]
            for i in range(1, rowNum):
                row.append(tri[rowNum - 1][i - 1] + tri[rowNum - 1][i])

            row.append(1)
            tri.append(row)

        return tri[-1]
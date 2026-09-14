class Solution:
    def projectionArea(self, grid):
        """
        :param grid: List[List[int]]
        :return: int
        """

        n = len(grid)
        xyArea = 0
        yzArea = 0
        zxArea = 0
        total = 0

        for i in range(n):
            maxRow = 0
            maxCol = 0
            for j in range(n):
                if grid[i][j] > 0:
                    xyArea += 1

                maxRow = max(maxRow, grid[i][j])
                maxCol = max(maxCol, grid[j][i])


            yzArea +=  maxRow

            zxArea += maxCol

        Total = xyArea + yzArea +zxArea

        return Total

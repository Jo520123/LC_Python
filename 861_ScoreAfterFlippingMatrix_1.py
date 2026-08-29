class Solution:
    def matrixScore(self, grid):
        """
        :param grid: List[List[int]]
        :return: int
        """
        row = len(grid)
        col = len(grid[0])


        for i in range(row):
            if grid[i][0] == 0:

                for j in range(col):
                    grid[i][j] = 1 - grid[i][j]


        for j in range(1, col):

            c_ones = sum(grid [i][j] for i in range(row))

            if c_ones < row/2:

                for i in range(row):

                    grid[i][j] = 1 - grid[i][j]


        Total_val = 0

        for i in range(row):
            row_val = 0

            for j in range(col):

                row_val = (row_val<<1) | grid[i][j]


            Total_val += row_val


        return Total_val

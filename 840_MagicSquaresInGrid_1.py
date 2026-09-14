class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :param grid: List[List[int]]
        :return: int
        """

        def matrix_check(r, c):
            num_list = []

            if grid[r+1][c+1] != 5:
                return False


            for i in range(3):
                for j in range(3):

                    num_list.append(grid[r+i][c+j])


            if sorted(num_list) != list(range(1,10)):
                return False


            for i in range(3):
                if sum(grid[r+i][c+j] for j in range(3)) != 15:
                    return False

                if sum(grid[r+j][c+i] for j in range(3)) != 15:
                    return False


            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15:
                return False

            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15:
                return False


            return True


        row, col = len(grid), len(grid[0])
        c = 0

        if row < 3 or col < 3:
            return 0

        for i in range(row-2):
            for j in range(col-2):
                if matrix_check(i,j):
                    c += 1


        return c

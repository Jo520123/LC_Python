class Solution:
    def getMaximumGold(self, grid):
        """
        :param grid: List[List[int]]
        :return: int
        """

        x, y = len(grid), len(grid[0])
        maxG = [0]


        def DFS(r,c, currentG):

            maxG[0] = max(maxG[0], currentG)

            temp = grid[r][c]
            grid[r][c] = 0

            for delta_r, delta_c in ((0,-1), (0,1),(1,0),(-1,0)):
                nr, nc = r + delta_r, c + delta_c

                if 0 <= nr < x and 0 <= nc < y and grid[nr][nc] > 0:

                    DFS(nr,nc, currentG + grid[nr][nc])

            grid[r][c] = temp



        for i in range(x):
            for j in range(y):
                if grid[i][j] > 0:
                    DFS(i, j, grid[i][j])

        return maxG[0]

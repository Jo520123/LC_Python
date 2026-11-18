class Solution:
    def numEnclaves(self, grid):
        """
        :param grid: list[list[int]]
        :return: int
        """

        m, n = len(grid), len(grid[0])

        def DFS(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0:
                return

            grid[r][c] = 0

            DFS(r+1, c)
            DFS(r-1, c)
            DFS(r, c+1)
            DFS(r, c-1)


        for c in range(n):
            if grid[0][c] == 1:
                DFS(0, c)

            if grid[m-1][c] == 1:
                DFS(m-1, c)

        for r in range(m):
            if grid[r][0] == 1:
                DFS(r, 0)

            if grid[r][n-1] == 1:
                DFS(r, n-1)


        count = 0

        for r in range(m):
            for c in range(n):

                if grid[r][c] == 1:
                    count += 1

        return count
class Solution:
    def countServers(self, grid):
        """
        :param grid: List[List[int]]
        :return: int
        """
        m, n = len(grid), len(grid[0])

        row = m * [0]
        col = n * [0]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1


        c = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row[i] > 1 or col[j] > 1:
                        c += 1

        return c

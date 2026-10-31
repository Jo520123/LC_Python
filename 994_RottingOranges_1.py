from collections import deque

class Solution:
    def orangesRotting(self, grid):
        """
        :param grid: list[list[int]]
        :return: int
        """

        m = len(grid)
        n = len(grid[0])

        freshCount = 0
        queue = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r,c))

                elif grid[r][c] == 1:
                    freshCount += 1

        if freshCount == 0:
            return 0

        time = 0

        direction = [(-1,0),(1,0),(0,1),(0,-1)]

        while queue:

            #print("queue = ", queue)

            for i in range(len(queue)):

            #print(len(queue))
            #print("len =" , len(queue))

                r, c = queue.popleft()
                #print(r,c)

                for delta_r, delta_c in direction:

                    nr , nc = r + delta_r, c + delta_c

                #print(nr, nc)

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:

                        grid[nr][nc] = 2
                        freshCount-= 1
                        queue.append((nr,nc))


            if queue:
                time += 1


        return time if freshCount == 0 else -1

from collections import deque

class Solution:
    def shortestBridge(self, grid):
        """
        :param grid: list[list[int]]
        :return: int
        """
        n = len(grid)
        que = deque()
        visited = set()

        def DFS(r,c):
            if (r >= n or c >= n or r < 0 or c < 0 or grid[r][c] == 0 or (r,c) in visited):
                return

            visited.add((r,c))
            que.append((r,c,0))

            for delta_r, delta_c in [(-1,0),(0,1),(0,-1),(1,0)]:
                DFS(r + delta_r, c + delta_c)


        check = False

        for r in range(n):
            if check:
                break

            for c in range(n):
                if grid[r][c] == 1:

                    DFS(r,c)

                    check = True

                    break

        while que:
            r , c , dis = que.popleft()

            for delta_r , delta_c in [(-1,0),(0,1),(0,-1),(1,0)]:

                b_dr = r + delta_r
                b_dc = c + delta_c

                if 0 <= b_dr < n and 0 <= b_dc < n and (b_dr, b_dc)not in visited:

                    if grid[b_dr][b_dc] == 1:

                        return dis

                    visited.add((b_dr, b_dc))

                    que.append((b_dr, b_dc , dis + 1))

        return -1

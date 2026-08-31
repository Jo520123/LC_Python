class Solution:
    def robotSim(self, commands, obstacles):
        """
        :param commands: List[int]
        :param obstacles: List[List[int]]
        :return: int
        """
        obs_tuple = set(tuple(x) for x in obstacles)

        d_x = [0,1,0,-1]
        d_y = [1,0,-1,0]
        x, y = 0, 0
        dir_s = 0
        max_sq = 0

        for com in commands:
            if com == -2:
               dir_s = (dir_s - 1) % 4

            elif com == -1:
                dir_s = (dir_s + 1) % 4

            else:

                for i in range(com):
                    n_x = x + d_x[dir_s]
                    n_y = y + d_y[dir_s]

                    if (n_x, n_y) in obs_tuple:
                        break

                    max_sq = max(max_sq, n_x*n_x + n_y*n_y)

                    x, y = n_x, n_y

        return max_sq

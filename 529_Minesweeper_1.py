class Solution:
    def updateBoard(self, board, click):
        """
        :param board:  List[List[str]]
        :param click: List[int]
        :return: List[List[str]]
        """
        r,c = click

        x, y = len(board), len(board[0])

        if board[r][c] == 'M':

            board[r][c] = 'X'

            return board

        def DFS1(row, col):

            count = 0

            for delta_r in [-1, 0, 1]:
                for delta_c in [-1, 0, 1]:
                    if delta_r == 0 and delta_c == 0:
                        continue

                    delta_rr, delta_cc = row + delta_r, col + delta_c

                    if 0 <= delta_rr < x and 0 <= delta_cc < y and board[delta_rr][delta_cc] == 'M':

                        count += 1


            if count > 0:
                board[row][col] = str(count)

            else:

                board[row][col] = 'B'

                for delta_r in [-1, 0, 1]:
                    for delta_c in [-1, 0, 1]:
                        if delta_r == 0 and delta_c == 0:
                            continue

                        delta_rr, delta_cc = row + delta_r, col + delta_c

                        if 0 <= delta_rr < x and 0 <= delta_cc < y and board[delta_rr][delta_cc] == 'E':
                            DFS1(delta_rr, delta_cc)


        DFS1(r,c)

        return board

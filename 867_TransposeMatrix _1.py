class Solution:
    def transpose(self, matrix):
        """
        :param matrix: List[List[int]]
        :return: List[List[int]]
        """
        mr, mc = len(matrix), len(matrix[0])

        transp_matrix = [[0] * mr for i in range(mc)]

        #print(transp_matrix)

        for i in range(mr):
            for j in range(mc):

                transp_matrix[j][i] =  matrix[i][j]


        return transp_matrix
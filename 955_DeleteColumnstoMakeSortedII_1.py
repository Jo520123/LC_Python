class Solution:
    def minDeletionSize(self, strs):
        """
        :param strs: list[str]
        :return: int
        """

        r = len(strs)
        c = len(strs[0])

        deleteC = 0

        sortedRow = (r-1) * [False]

        #print(sortedRow)

        for i in range(c):

            delete = False

            for j in range(r-1):

                if not sortedRow[j] and strs[j][i] > strs[j+1][i]:

                    delete = True

                    break

            if delete:
                deleteC += 1

            else:
                for j in range(r-1):

                    if not sortedRow[j] and strs[j][i] < strs[j+1][i]:

                        sortedRow[j] = True


        return deleteC


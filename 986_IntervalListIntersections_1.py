class Solution:
    def intervalIntersection(self, firstList, secondList):
        """
        :param firstList: list[list[int]]
        :param secondList: list[list[int]]
        :return: list[list[int]]
        """

        res = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):

            startMax = max(firstList[i][0], secondList[j][0])
            endMin = min(firstList[i][1], secondList[j][1])

            if startMax <= endMin:
                res.append([startMax,endMin])


            if firstList[i][1] < secondList[j][1]:
                i += 1

            else:

                j += 1


        return res
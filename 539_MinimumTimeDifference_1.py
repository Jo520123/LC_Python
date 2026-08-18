class Solution:
    def findMinDifference(self, timePoints):
        """
        :param timePoints: List[str]
        :return: int
        """

        if len(timePoints) > 1440:
            return 0

        minutes = []

        for x in timePoints:
            h, m = map(int, x.split(':'))

            minutes.append(h * 60 + m)

        minutes.sort()

        minDiff = (1440 - minutes[-1]) + minutes[0]

        for i in range(1, len(minutes)):
            Diff = minutes[i] - minutes[i-1]

            if Diff < minDiff:
                minDiff = Diff


        return minDiff

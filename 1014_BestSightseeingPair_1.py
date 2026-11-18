class Solution:
    def maxScoreSightseeingPair(self, values):
        """
        :param values: list[int]
        :return: int
        """

        max_score = 0

        prev = values[0] + 0

        for j in range(1, len(values)):

            max_score = max(max_score, prev + values[j] - j)


            prev = max(prev, values[j] + j)


        return max_score
class Solution:
    def findRelativeRanks(self, score):
        """
        :param score: List[int]
        :return: List[str]
        """

        l = len(score)

        ans = [""] * l

        AthleteS_idx = [(score[i], i) for i in range(l)]

        AthleteS_idx.sort(reverse = True, key = lambda x : x[0])

        for x, (y, z) in enumerate(AthleteS_idx,start = 1):
            if x == 1 :
                ans[z] = "Gold Medal"

            elif x == 2:
                ans[z] = "Silver Medal"

            elif x == 3:
                ans[z] = "Bronze Medal"

            else:
                ans[z] = str(x)

        return ans

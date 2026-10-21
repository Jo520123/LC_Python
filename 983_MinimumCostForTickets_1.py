class Solution:
    def mincostTickets(self, days, costs):
        """
        :param days: list[int]
        :param costs: list[int]
        :return: int
        """

        uniqueDay = set(days)

        lastDate = days[-1]

        dp = [0] * (lastDate + 1)


        for i in range(1, lastDate + 1):

            if i not in uniqueDay:

                dp[i] = dp[i-1]

            else:

                cost1D = dp[i-1] + costs[0]

                cost7D = dp[max(0, i-7)] + costs[1]

                cost30D = dp[max(0, i-30)] + costs[2]

                dp[i] = min(cost1D, cost7D, cost30D)


        return dp[lastDate]
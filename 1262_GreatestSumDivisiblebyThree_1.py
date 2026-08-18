class Solution:
    def maxSumDivThree(self, nums):
        """

        :param nums: List[int]
        :return: int
        """

        dp = [0,0,0]

        for x in nums:
            tem_dp = dp.copy()

            for y in tem_dp:
                s = y + x
                rem = s % 3

                dp[rem] = max(dp[rem],s)

        return dp[0]

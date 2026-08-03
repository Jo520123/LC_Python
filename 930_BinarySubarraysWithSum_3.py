
class Solution:
    def numSubarraysWithSum(self, nums, goal):
        """
        :param nums: List[int]
        :param goal:int
        :return:int
        """

        def TT(self, goal):
            if goal < 0:
                return 0

            c = 0
            Total = 0
            l = 0


            for i in range(len(nums)):
                Total += nums[i]

                while Total > goal:
                    Total -= nums[l]
                    l += 1


                c += (i - l + 1)

            return c


        return TT(self, goal) - TT(self, goal-1)
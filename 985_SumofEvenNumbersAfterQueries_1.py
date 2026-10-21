class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        """
        :param nums: list[int]
        :param queries: list[list[int]]
        :return: list[int]
        """

        evenSum = sum(x for x in nums if x%2 == 0)

        res = []


        for val, idx in queries:

            currentV = nums[idx]

            if currentV %2 == 0:
                evenSum -= currentV

            nums[idx] += val

            if nums[idx] %2 == 0:

                evenSum += nums[idx]


            res.append(evenSum)

        return res

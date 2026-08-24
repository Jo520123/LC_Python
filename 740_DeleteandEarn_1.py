class Solution:
    def deleteAndEarn(self, nums):

        """
        :param nums: List[int]
        :return: int

        """
        if not nums:
            return 0

        MaxV = max(nums)

        sum_acc = [0] * (MaxV+1)

        for x in nums:
            sum_acc[x] += x

        if MaxV == 0:
            return 0

        if MaxV == 1:
            return sum_acc[1]

        pre1 = max(sum_acc[0], sum_acc[1])

        pre2 = sum_acc[0]

        for i in range(2, len(sum_acc)):
            current = max(pre1, pre2 + sum_acc[i])
            pre2 = pre1
            pre1 = current


        return pre1

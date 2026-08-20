class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :param nums: List[int]
        :param k: int
        :return: bool
        """

        dic_rem = {0:-1}
        sum = 0

        for i, value in enumerate(nums):
            sum += value

            rem = sum % k

            if rem in dic_rem:
                if i - dic_rem[rem] >= 2:
                    return True
            else:
                dic_rem[rem] = i

        return False

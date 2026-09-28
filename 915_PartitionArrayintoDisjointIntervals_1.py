class Solution:
    def partitionDisjoint(self, nums):
        """
        :param nums: list[int]
        :return: int
        """

        n = len(nums)
        min_right = [0] * n

        min_right[-1] = nums[-1]

        for i in range(n-2, -1, -1):
            min_right[i] = min(min_right[i+1], nums[i])


        max_left = 0

        for i in range(n):
            max_left = max(max_left, nums[i])

            if max_left <= min_right[i+1]:

                return i + 1

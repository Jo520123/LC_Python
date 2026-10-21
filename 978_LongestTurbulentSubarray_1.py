class Solution:
    def maxTurbulenceSize(self, arr):
        """
        :param arr: list[int]
        :return: int
        """

        res = 1
        decrease = 1
        increase = 1

        n = len(arr)

        for i in range(1,n):

            if arr[i] > arr [i-1]:
                increase = decrease + 1
                decrease = 1

            elif arr[i] < arr[i-1]:
                decrease = increase + 1
                increase = 1

            else:
                decrease = 1
                increase = 1

            res = max(res, increase, decrease)

        return res
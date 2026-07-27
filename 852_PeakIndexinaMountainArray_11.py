class Solution:

    def peakIndexInMountainArray(self, arr):
        """
        :param arr: List[int]
        :return: int
        """

        n = len(arr)

        l, r = 0, n-1


        while l < r:

            mid = (l + r) // 2

            if arr[mid] < arr[mid+1]:

                l = mid+1

            else:
                r = mid

        return l

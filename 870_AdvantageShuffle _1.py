class Solution:
    def advantageCount(self, nums1, nums2):
        """

        :param nums1: List[int]
        :param nums2: List[int]
        :return: List[int]
        """

        nums1.sort()

        n = len(nums1)

        l, r = 0, n-1

        res = [0] * n

        nums2_s = sorted((val,idx) for idx, val in enumerate(nums2))

        for i in range(len(nums2_s)-1, -1, -1):

            val, idx = nums2_s[i]

            if nums1[r] > val:

                res[idx] = nums1[r]

                r-= 1

            else:

                res[idx] = nums1[l]

                l += 1

        return res

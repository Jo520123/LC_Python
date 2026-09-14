class Solution:
    def maxSubarraySumCircular(self, nums):
        """
        :param nums: List[int]
        :return: int
        """

        Total = 0
        c_M = 0
        c_m = 0
        M_s = nums[0]
        m_s = nums[0]


        for x in nums:
            c_M = max(c_M + x, x)
            M_s = max(M_s, c_M)

            c_m = min(c_m + x, x)
            m_s = min(m_s, c_m)

            Total += x

        if M_s < 0:
            return M_s


        return max(M_s, Total - m_s)

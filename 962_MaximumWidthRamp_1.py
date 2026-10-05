class Solution:
    def maxWidthRamp(self, nums):
        """
        :param nums: list[int]
        :return: int
        """

        n = len(nums)
        stack = []
        maxLen = 0

        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)


        for j in range(n-1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:

                maxLen = max(maxLen, j-stack.pop())
 

        return maxLen

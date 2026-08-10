class Solution:
    def find132pattern(self, nums):
        """
        :param nums: List[int]
        :return: bool
        """
        if len(nums) < 3:
            return False

        S = []
        compareV = float('-inf')

        for x in reversed(nums):
            if x < compareV:
                return True


            while S and S[-1] < x:
                compareV = S.pop()

            S.append(x)

        return False

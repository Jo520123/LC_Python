from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        """
        :param nums: List[int]
        :return: str
        """

        tranfStr = list(map(str,nums))

        res = ""

        def compare(x, y):
            if x + y > y + x:
                return -1

            elif x + y < y + x:
                return 1

            else:
                return 0


        tranfStr.sort(key = cmp_to_key(compare))

        if tranfStr[0] == "0":
            return "0"

        return "".join(tranfStr)


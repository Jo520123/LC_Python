

class Solution:
    def reverseOnlyLetters(self, s):
        """
        :param s: str
        :return: str
        """

        C_list = list(s)

        l ,r = 0, len(s)-1


        while l < r:
            if not C_list[l].isalpha():
                l += 1

            if not C_list[r].isalpha():
                 r -= 1

            else:
                C_list[l], C_list[r] = C_list[r], C_list[l]
                l += 1
                r -= 1

        return "".join(C_list)

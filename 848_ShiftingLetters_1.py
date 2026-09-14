class Solution:
    def shiftingLetters(self, s, shifts):
        """
        :param s:str
        :param shifts:List[int]
        :return:str
        """

        n = len(s)
        shift_length = 0
        ans = list(s)

        for i in range(n-1, -1, -1):
            shift_length += shifts[i]

            new_char_length = ((ord(ans[i]) - ord('a')) + shift_length) % 26

            ans[i] = chr(ord('a') + new_char_length)

        return "".join(ans)

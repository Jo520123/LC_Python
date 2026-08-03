class Solution:
    def licenseKeyFormatting(self, s, k):
        """
        :param s: str
        :param k: int
        :return:str
        """

        lis =[]
        c = 0

        s_tru = s.replace("-" , "").upper()

        for i in range(len(s_tru)-1, -1, -1):
            if c == k:
                lis.append("-")
                c = 0

            lis.append(s_tru[i])
            c += 1

        return "".join(reversed(lis))

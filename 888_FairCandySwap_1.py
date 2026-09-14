class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :param aliceSizes: List[int]
        :param bobSizes: List[int]
        :return: List[int]
        """

        A_Total = sum(aliceSizes)
        B_Total = sum(bobSizes)

        dif = (B_Total - A_Total)//2

        print("1111111111111111111111111111111111111")
        print("B-A", B_Total -A_Total)
        print("A-B",A_Total - B_Total)
        print("1111111111111111111111111111111111111")

        bobSizes_set = set(bobSizes)


        for x in aliceSizes:
            y = x + dif

            if y in bobSizes_set:

                return [x, y]

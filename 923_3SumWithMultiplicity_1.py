class Solution:
    def threeSumMulti(self, arr, target):
        """
        :param arr: List[int]
        :param target: int
        :return: int
        """


        MOD = 10**9 +7

        number_list = [0] * 101

        res = 0

        for x in arr:
            number_list[x] += 1


        for i in range(101):
            for j in range(i, 101):

                k = target - i - j

                if k > 100 or k < j:
                    continue

                if number_list[i] == 0 or number_list[j] == 0 or number_list[k] == 0:
                    continue


                if i < j < k:

                    res += number_list[i] * number_list[j] * number_list[k]


                elif i == j and j < k:

                    res += (number_list[i] * (number_list[i] - 1)//2) * number_list[k]

                elif i < j and j == k:

                    res += number_list[i] * (number_list[j] * (number_list[j]-1)//2)


                elif i == j == k:

                    res += (number_list[i] * (number_list[i] -1) * (number_list[i] -2))//6


                res %= MOD


        return res

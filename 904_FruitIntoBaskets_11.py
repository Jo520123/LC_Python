
class Solution:
    def totalFruit(self, fruits):
        """
        :param fruits: List[int]
        :return: int
        """

        basket = {}
        l = 0
        MaxNum = 0

        n = len(fruits)


        for i in range(n):
            f = fruits[i]
            basket[f] = basket.get(f, 0) + 1

            while len(basket) > 2:
                basket[fruits[l]] -= 1

                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]

                l += 1

            MaxNum = max(MaxNum, i-l +1)

        return MaxNum
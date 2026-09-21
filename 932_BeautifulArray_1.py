class Solution:
    def beautifulArray(self, n):
        """
        :param n: int
        :return: list[int]
        """

        res = [1]
      

        while len(res) < n:
            res = [2*x for x in res] + [2 * x -1 for x in res]

        return [x for x in res if x <= n]


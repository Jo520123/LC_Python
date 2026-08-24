from collections import defaultdict

class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :param richer: List[List[int]]
        :param quiet: List[int]
        :return: List[int]
        """


        l = len(quiet)
        res = [-1] * l

        dic = defaultdict(list)


        for u,v in richer:
            dic[v].append(u)


        def DFS(x):
            if res[x] != -1:
                return res[x]

            min_qp = x

            for richer in dic[x]:

                cand = DFS(richer)

                if quiet[cand] < quiet[min_qp]:

                    min_qp = cand

            res[x] = min_qp

            return res[x]


        for i in range(l):
            DFS(i)

        return res

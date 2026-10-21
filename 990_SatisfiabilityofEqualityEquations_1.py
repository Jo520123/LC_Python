class Solution:
    def equationsPossible(self, equations):
        """
        :param equations: list[str]
        :return: bool
        """

        parent_dic = {}


        def find(x):
            if x not in parent_dic:
                parent_dic[x] = x

            if parent_dic[x] == x:
                return x

            parent_dic[x] = find(parent_dic[x])

            return parent_dic[x]


        def Union(x,y):

            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                parent_dic[rootX] = rootY


        for e in equations:
            if e[1] == "=":
                x = find(e[0])
                y = find(e[3])

                Union(x,y)


        for e in equations:
            if e[1] == "!":
                x = e[0]
                y = e[3]

                if find(x) == find(y):
                    return False


        return True
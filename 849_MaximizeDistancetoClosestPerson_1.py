class Solution:
    def maxDistToClosest(self, seats):
        """
        :param seats: List[int]
        :return:int
        """
        lp = -1
        l = len(seats)
        max_dst = 0

        for i in range(l):
            if seats[i] == 1:
                if lp == -1:
                    max_dst = i

                else:
                    max_dst = max(max_dst, (i-lp)//2)

                lp = i

        max_dst = max(max_dst, (l-1)-lp)


        return max_dst

class Solution:
    def minAreaFreeRect(self, points):
        """
        :param points: list[list[int]]
        :return: float
        """

        n = len(points)
        minArea = float("inf")
        pointTuple = set(tuple(x) for x in points)


        for i in range(n):
            vertex1 = points[i]

            for j in range(n):
                if i == j:
                    continue

                vertex2 = points[j]

                for k in range(n):

                    if k == i or k == j:
                        continue

                    vertex3 = points[k]


                    v21_x = vertex2[0] - vertex1[0]
                    v21_y = vertex2[1] - vertex1[1]

                    v31_x = vertex3[0] - vertex1[0]
                    v31_y = vertex3[1] - vertex1[1]


                    if v21_x * v31_x + v21_y*v31_y == 0:
                        vertex4 = (vertex3[0] + v21_x , vertex3[1] + v21_y)

                        if vertex4 in pointTuple:

                            area = (v21_x**2 + v21_y**2)**0.5 * (v31_x**2 + v31_y**2)**0.5

                            minArea = min(minArea, area)


        return minArea if minArea != float("inf") else 0.0
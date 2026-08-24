class Solution:
    def carFleet(self, target, position, speed):
        """
        :param target: int
        :param position: List[int]
        :param speed: List[int]
        :return: int
        """

        posDes = sorted(zip(position,speed), reverse = True)
        fleets = 0
        max_t = 0

        for p, s in posDes:

            tg = (target-p)/s

            if tg > max_t:
                fleets += 1
                max_t = tg

        return fleets



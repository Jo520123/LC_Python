class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        """
        :param time:List[int]
        :return: int
        """

        c = 0
        reaminder_arr = [0] * 60

        for x in time:
            rem = x % 60

            complement = (60 - rem) % 60

            c += reaminder_arr[complement]

            reaminder_arr[rem] += 1

        return c
class Solution:
    def numRescueBoats(self, people, limit):
        """
        :param people: List[int]
        :param limit: int
        :return: int
        """
        people.sort()

        l, r = 0, len(people)-1

        c = 0

        while l <= r:

            if people[l] + people[r] <= limit:
                l += 1

            r -= 1
            c += 1

        return c

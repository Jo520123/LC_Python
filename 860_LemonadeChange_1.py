class Solution:
    def lemonadeChange(self, bills):
        """
        :param bills: List[int]
        :return: bool
        """

        five, ten = 0, 0

        for x in bills:
            if x == 5:
                five += 1

            elif x ==10:
                if five > 0:
                    five -= 1
                    ten += 1

                else:
                    return False

            else:

                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1

                elif five >= 3:
                    five -= 3

                else:
                    return False

        return True

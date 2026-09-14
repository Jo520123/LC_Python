class Solution:
    def numSpecialEquivGroups(self, words):
        """
        :param words: List[str]
        :return: int
        """

        uniq_signature = set()


        for w in words:
            even = sorted(w[0::2])
            odd = sorted(w[1::2])

            combine_tuple = (tuple(even),tuple(odd))
            uniq_signature.add(combine_tuple)

        count = len(uniq_signature)

        return count

from collections import Counter
class Solution:
    def wordSubsets(self, words1, words2):
        """
        :param words1: List[str]
        :param words2: List[str]
        :return: List[str]
        """

        w2_count = Counter()


        for w in words2:
            w2_sub_count = Counter(w)

            for chr, num in w2_sub_count.items():
                w2_count[chr] = max(num, w2_count[chr])


        res = []

        for w in words1:
            w1_count = Counter(w)

            if all(w1_count[chr] >= num for chr, num in w2_count.items()):
                res.append(w)

        return res
		
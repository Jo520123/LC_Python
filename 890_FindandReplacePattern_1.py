class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :param words: List[str]
        :param pattern: str
        :return: List[str]
        """

        def signature_pattern(pattern):
            dic = {}
            unique_signature = []

            for char in pattern:

                if char not in dic:
                    dic[char] = len(dic)

                unique_signature.append(dic[char])


            return tuple(unique_signature)


        patt_sig = signature_pattern(pattern)

        return [w for w in words if signature_pattern(w) == patt_sig]

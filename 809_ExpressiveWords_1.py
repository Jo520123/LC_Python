class Solution:
    def expressiveWords(self, s, words):
        """
        :param s: str
        :param words: List[str]
        :return: int
        """


        def RLE(s):

            res = []
            if not s:
                return res

            char = s[0]
            c = 1

            for i in range(1, len(s)):
                if s[i] == char:
                    c += 1

                else:
                    res.append((char, c))

                    char = s[i]

                    c = 1

            res.append((char, c))

            return res


        s_tuple_RLE= RLE(s)
        stretchy_c = 0


        for word in words:
            w_tuple_RLE = RLE(word)

            if len(w_tuple_RLE) != len(s_tuple_RLE):
                continue

            isStretchy = True


            for (sc,s_len),(wc,w_len) in zip(s_tuple_RLE,w_tuple_RLE):
                if sc != wc and w_len > s_len:

                    isStretchy = False

                    break

                if w_len < s_len and s_len < 3:

                    isStretchy = False

                    break

            if isStretchy:
                stretchy_c += 1


        return stretchy_c

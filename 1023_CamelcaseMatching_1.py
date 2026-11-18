class Solution:
    def camelMatch(self, queries, pattern):
        """
        :param queries: list[str]
        :param pattern: str
        :return: list[bool]
        """

        def Match(query, pattern):
            i = 0
            n = len(pattern)

            for x in query:
                if i < n and x == pattern[i]:
                    i += 1

                elif x.isupper():

                    return False

            return i == n

        return [Match(query, pattern) for query in queries]


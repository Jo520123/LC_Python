from bisect import bisect_left

class Solution:
    def suggestedProducts(self, products, searchWord):
        """
        :param products: List[str]
        :param searchWord: str
        :return:List[List[str]]
        """

        res = []
        prefix = ""
        products.sort()

        for x in searchWord:
            prefix += x

            idx = bisect_left(products,prefix)

            suggestion = []

            for i in range(idx, min(idx+3, len(products))):

                if products[i].startswith(prefix):
                    suggestion.append(products[i])

                else:
                    break

            res.append(suggestion)

        return res

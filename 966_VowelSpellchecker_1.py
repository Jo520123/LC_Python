class Solution:
    def spellchecker(self, wordlist , queries):
        """
        :param wordlist: list[str]
        :param queries: list[str]
        :return: list[str]
        """

        unique_dic = set(wordlist)
        mask_vowel_dic = {}
        case_insensitive_dic = {}

        def mask_vowel(word):
            vowel_set = set("aeiou")

            res = ""

            for w in word:
                if w.lower() in vowel_set:
                    res += "*"
                else:
                    res += w.lower()


            return res


        for w in wordlist:

            if w.lower() not in case_insensitive_dic:
                case_insensitive_dic[w.lower()] = w


            if mask_vowel(w) not in mask_vowel_dic:
                mask_vowel_dic[mask_vowel(w)] = w

        ans = []

        for q in queries:
            if q in unique_dic:
                ans.append(q)

            elif q.lower() in case_insensitive_dic:
                ans.append(case_insensitive_dic[q.lower()])

            elif mask_vowel(q) in mask_vowel_dic:
                ans.append(mask_vowel_dic[mask_vowel(q)])

            else:
                ans.append("")

        return ans

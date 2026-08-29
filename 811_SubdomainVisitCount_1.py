from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains):
        """

        :param cpdomains: List[str]
        :return: List[str]
        """

        dic = defaultdict(int)

        for domains in cpdomains:
            #print(domains)
            #print(domains.split())
            c_str, dom = domains.split()

            c_int = int(c_str)

            #print(dom)

            subd_s = dom.split(".")

            #print(subd_s)


            #for subd in dom:
                #print(subd)
                #subd_s = subd.split(".")
                #print(subd_s[0])
                #print(subd_s)


            for i in range(len(subd_s)):
                sub_domain = ".".join(subd_s[i:])
                dic[sub_domain] += c_int

            print(dic)

            return [f"{y} {x}" for x, y in dic.items()]

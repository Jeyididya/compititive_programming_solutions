class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        di = {}
        for cc in cpdomains:
            num, dom = cc.split()
            domains = dom.split(".")[::-1]
            for i in range(len(domains)):
                dd = ""  # ".".join(domains[:i+1])
                for ad in domains[:i+1]:
                    dd = ad+"."+dd
                dd = dd[:-1]
                if dd in di:
                    di[dd] += int(num)
                else:
                    di[dd] = int(num)
        ans = [str(di[i])+" "+i for i in di]
        return ans

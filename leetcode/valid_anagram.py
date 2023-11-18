class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        slen = len(s)
        tlen = len(t)

        # minlen=0
        # if slen < tlen:
        #     minlen = slen
        # else:
        #     minlen = tlen
        # print(minlen, slen, tlen)
        if slen == tlen:
            for i in range(slen):
                if s[i] != t[i]:
                    return False
            return True
        else:
            return False

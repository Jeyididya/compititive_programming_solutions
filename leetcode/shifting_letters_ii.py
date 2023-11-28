class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        lii = [0]*(n+1)
        for x, y, z in shifts:
            if z == 1:
                lii[x] += 1
                lii[y+1] -= 1
            else:
                lii[x] -= 1
                lii[y+1] += 1
        for i in range(1, n):
            lii[i] += lii[i-1]
        an = ""
        oo = ord("a")
        for i in range(len(s)):
            cu = (ord(s[i])-oo+lii[i]) % 26
            an = an+chr(cu+oo)
        print(an)
        return an
        # ll=[0 for i in s]
        # for i in shifts:
        #     if i[2]==0:
        #         temps=s[i[0]:i[1]+1]
        #         temps=[chr(ord(l)+1) for l in temps]

        #     elif i[2]==1:
        #         pass
        return s

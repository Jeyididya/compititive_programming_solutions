class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        from math import sqrt
        n = int(sqrt(c))+1
        li = [i for i in range(n+1)]

        fi = 0
        la = len(li)-1
        while fi <= la:
            sq = li[fi]*li[fi]+li[la]*li[la]
            if sq == c:
                return True
            elif sq < c:
                fi += 1
            elif sq > c:
                la -= 1
        return False

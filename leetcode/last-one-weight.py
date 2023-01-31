class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            cpy=stones.copy()
            cpy.sort()
            ma=cpy[-1]
            secma=cpy[-2]
            if ma==secma:
                stones.remove(ma)
                stones.remove(secma)
            else:
                stones.remove(secma)
                ind=stones.index(ma)
                stones[ind]=ma-secma
            print(stones)
        if len(stones)==1:
            return stones[0]
        else:
            return 0
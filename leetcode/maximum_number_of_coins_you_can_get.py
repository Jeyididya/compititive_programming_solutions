class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        alice = 0
        me = 0
        bob = 0

        i = 0
        j = len(piles)-1
        k = j-1
        while True:
            if j-2 != i:
                print(i, j, k)
                alice += piles[j]
                me += piles[k]
                bob += piles[i]
                i += 1
                j -= 2
                k -= 2
            else:
                alice += piles[j]
                me += piles[k]
                bob += piles[i]
                break
        return me

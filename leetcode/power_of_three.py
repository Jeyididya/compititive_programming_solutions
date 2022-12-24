class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        num=1
        i=0
        while num<n:
            num=pow(3,i)
            i+=1
        if num==n:
            return True
        return False
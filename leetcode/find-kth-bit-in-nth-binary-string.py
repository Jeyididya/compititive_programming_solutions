class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        for i in range(n-1):
            s=s+"1"+str(self.invert(s))[::-1]
        print(s)
        return s[k-1]
    def invert(self,st) -> str:
        ss=""
        for i in st:
            if i=="0":
                ss+="1"
            else:
                ss+="0"
        return ss
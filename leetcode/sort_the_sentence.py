class Solution:
    def sortSentence(self, s: str) -> str:
        lis=[]
        for i in s.split():
            lis.append([int(i[-1]),i[:-1]])
        lis.sort()
        sent=""
        for i in lis:
            sent+=i[1]+" "
        return sent[:-1]
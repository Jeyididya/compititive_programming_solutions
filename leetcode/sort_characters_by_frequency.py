class Solution:
    def frequencySort(self, s: str) -> str:
        di={}
        for i in s:
            try:
                di[i]+=1
            except:
                di[i]=1
        nl=[[di[i], i] for i in di]
        nl.sort(reverse=True)
        re=""
        for i in nl:
            re+=i[1]*i[0]
        return re
        #nl=[[s.count(i), i] for i in s]
        #nl.sort(reverse=True)
        #return [i[1] for i in nl ]


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        li=[]
        for i in trips:
            li.append([i[1],1,i[0]])
            li.append([i[2],0,i[0]])
        li.sort()
        print(li)
        pas=0
        for i in li:
            if i[1]==1:
                if pas+i[2]>capacity:
                    return False
                pas+=i[2]
            else:
                pas-=i[2]
        return True
                

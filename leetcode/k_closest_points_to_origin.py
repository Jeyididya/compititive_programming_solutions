from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        li=[]
        for i in points:
            dis=sqrt(pow(i[0],2)+pow(i[1],2))
            
            li.append([dis,i])
        li.sort()
        ans=[]
        for i in range(k):
            ans.append(li[i][1])
        return ans
class Solution:
  def findAnagrams(self, s: str, p: str) -> List[int]:
    count=0
    k=len(p)
    curr=s[:k]
    subar=[]
    ans=[]
    p=sorted(p)
    if sorted(curr)==p:
      subar.append(curr)
      ans.append(0)
    for i in range(1,len(s)-k+1):
      curr=curr[1:]#-s[i-1]
      curr=curr+s[i+k-1]
      # print(curr,set(curr),set(p))
      if sorted(curr)==p:
        subar.append(curr)
        ans.append(i)
    # print(subar)
    return ans
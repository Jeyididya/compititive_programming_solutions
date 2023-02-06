class Solution:
  def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
    count=0
    curr=sum(arr[:k])
    subar=[]
    if curr>=k*threshold:
        subar.append(curr)
    for i in range(1,len(arr)-k+1):
        curr=curr-arr[i-1]
        curr=curr+arr[i+k-1]
        print(curr,k*threshold,curr>k*threshold)
        if curr>=k*threshold:
            subar.append(curr)
    return len(subar)
        
            
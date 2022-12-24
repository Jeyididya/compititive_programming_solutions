class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        se=set(nums)
        freq=[]
        for i in se:
            freq.append([nums.count(i),i])
        freq.sort()
        ans=[]
        for i in freq[-k:]:
            ans.append(i[1])
        return ans
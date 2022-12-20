class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cop=nums.copy()
        cop.sort()
        ans=[]
        for i in nums:
            ans.append(cop.index(i))
        return ans
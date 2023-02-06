class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cou=0
        lef=[0]*len(nums)
        rig=[0]*len(nums)
        for i in range(1,len(nums)):
            if nums[i-1]==1:
                lef[i]=lef[i-1]+1
        for i in range(len(nums)-2,-1,-1):
            if nums[i+1]==1:
                rig[i]=rig[i+1]+1
        print(lef)
        print(rig)
        ma=0
        for i in range(len(lef)):
            if lef[i]+rig[i]>ma:
                ma=lef[i]+rig[i]
        return ma

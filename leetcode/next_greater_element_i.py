class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            ind=nums2.index(i)
            fl=False
            for j in range(ind,len(nums2)):
                
                if nums2[j]>i:
                    ans.append(nums2[j])
                    fl=True
                    break
            if not fl:
                ans.append(-1)
            
        return ans
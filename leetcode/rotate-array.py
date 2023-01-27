class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate(arr,i,j):
            while i<j:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
            return arr
        k=k%len(nums)
        if len(nums)!=1:
            rotate(nums,0,len(nums)-1)
            rotate(nums,0,k-1)
            rotate(nums,k,len(nums)-1)
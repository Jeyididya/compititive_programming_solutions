class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prevSum = {}
        res = 0
        currsum = 0
        for i in range(0, len(nums)): 
            currsum += nums[i]
            if currsum == k: 
                res += 1       
            if (currsum - k) in prevSum:
                res += prevSum[currsum - k]
            if currsum in prevSum:
                prevSum[currsum] += 1
            else:
                prevSum[currsum]=1
        return res
            
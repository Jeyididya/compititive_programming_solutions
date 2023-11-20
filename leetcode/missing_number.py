class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ll = len(nums)
        _sum = sum(nums)
        ans = (ll*(ll+1))/2 - _sum
        return ans

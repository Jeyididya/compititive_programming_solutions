class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nn = nums.copy()
        # nn =list(set(nn))
        nn.sort()
        di = {}

        for i in range(len(nn)):
            if nn[i] in di:
                di[nn[i]] = min(i+1, di[nn[i]])
            else:
                di[nn[i]] = i+1
        # print(di)
        ans = [di[i]-1 for i in nums]
        return ans

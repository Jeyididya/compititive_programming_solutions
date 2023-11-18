class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i=0
        # j=1
        # while j<=len(nums)-1:
        #     print(i,j)
        #     if nums[i]+nums[j] ==target:
        #         return [i,j]
        #     i+=1
        #     j+=1
        di = {}
        for i in range(len(nums)):
            if nums[i] in di:
                return [i, di[nums[i]][1]]
            else:
                di[target - nums[i]] = [nums[i], i]
            # print(di)

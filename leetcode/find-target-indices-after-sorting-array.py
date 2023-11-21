class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        coun = nums.count(target)
        ans = []
        if coun != 0:
            ind = nums.index(target)

            for i in range(1, coun+1):
                ans.append(ind)
                ind += 1
        return ans

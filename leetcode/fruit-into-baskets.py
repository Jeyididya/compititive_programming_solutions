class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        nums={}
        res=0
        # collections.Counter(
        for r in range(len(fruits)):
            if fruits[r] in nums.keys():
                nums[fruits[r]] += 1
            else:
                nums[fruits[r]] = 1
            while len(nums) > 2:
                if fruits[l] in nums.keys():
                    nums[fruits[l]] -= 1
                else:
                    nums[fruits[l]] -= -1
                if not nums[fruits[l]]:
                    nums.pop(fruits[l])
                l += 1
            res = max(res, r - l + 1)
        return res
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        a = [0]
        for i in range(len(arr)):
            a.append(a[-1]^arr[i])
        res = []
        for i in queries:
            res.append(a[i[1]+1]^a[i[0]])
        return res
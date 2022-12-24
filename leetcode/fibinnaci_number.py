class Solution:
    def fib(self, n: int) -> int:
        fibs=[0,1]
        for i in range(2,40):
            fibs.append(fibs[i-2]+fibs[i-1])
        return fibs[n]
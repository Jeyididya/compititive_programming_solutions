class Solution(object):
    def isSelfDividin(self, n):
        digits = []
        for i in str(n):
            if i == "0":
                return False
            else:
                digits.append(int(i))
        for i in digits:
            if n % i != 0:
                return False
        return True

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for i in range(left, right+1):
            if self.isSelfDividin(i):
                ans.append(i)
        return ans

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        pos = 2147483647
        neg = -2147483648
        ans = ""
        x = str(x)
        if x[0] == "-":
            ans = "-"+x[1:][::-1]
        else:
            ans = x[::-1]
        ans = int(ans)
        if ans < neg or ans > pos:
            return 0
        else:
            return ans

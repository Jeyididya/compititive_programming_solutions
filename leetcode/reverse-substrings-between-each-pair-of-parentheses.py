class Solution:
    def reverseParentheses(self, s: str) -> str:
        num=len(s)
        stack = []
        for i in range(num):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                j = stack.pop()
                s = s[:j] + s[j: i+1][::-1] + s[i+1:]

        s = s.replace('(', '')
        s = s.replace(')', '')
        return s
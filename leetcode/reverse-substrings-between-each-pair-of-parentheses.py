class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in s:
            temp=""
            if i !=")":
                stack.append(i)
            elif i ==")":
                a=stack.pop()
                while a!="(":
                    temp+=a
                    a=stack.pop()
                stack.append(temp[::-1])
        return stack[0][::-1]
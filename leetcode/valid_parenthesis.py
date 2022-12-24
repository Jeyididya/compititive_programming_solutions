class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)%2!=0:
            return False
        for i in s:
            if i in ["(","[","{"]:
                stack.append(i)
            elif len(stack)==0:
                return False
            elif i ==")" and stack[-1]=="(":
                stack.pop()
            elif i == "]" and  stack[-1]=="[":
                stack.pop()
            elif i == "}" and  stack[-1]=="{":
                stack.pop()
            else:
                return False
        if len(stack)>0:
            return False
        return True
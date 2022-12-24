class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=""
        tokens=tokens[::-1]
        stack=[]
        i=len(tokens)-1
        for i in range(len(tokens)-1,-1,-1):
            if tokens[i] in ["+", "-", "*", "/"]:
                op=stack.pop()
                op1=stack.pop()
                stack.append(int(eval(str(op1)+tokens[i]+str(op))))
            else:
                stack.append(tokens[i])

        return int(stack[0])
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j=0
        lt=[]
        for i in pushed:
            lt.append(i)
            while len(lt)>0 and popped[0]==lt[-1]:
                lt.pop()
                popped.pop(0)
        if len(lt)>0:
            return False
        return True
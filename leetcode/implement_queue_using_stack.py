class MyQueue:

    def __init__(self):
        self.queue=[]

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        xl=self.queue.pop(0)
        return xl

    def peek(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        if len(self.queue)==0:
            return True
        return False
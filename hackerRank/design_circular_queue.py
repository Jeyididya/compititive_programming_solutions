class MyCircularDeque:

    def __init__(self, k: int):
        self.qu=[]
        self.size=k
        

    def insertFront(self, value: int) -> bool:
        if len(self.qu)<self.size:
            self.qu.insert(0,value)
            return True
        else:
            return False
    def insertLast(self, value: int) -> bool:
        if len(self.qu)<self.size:
            self.qu.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        try:
            self.qu.pop(0)
            return True
        except:
            return False
        

    def deleteLast(self) -> bool:
        try:
            self.qu.pop()
            return True
        except:
            return False

    def getFront(self) -> int:
        try:
            return self.qu[0]
        except:
            return -1

    def getRear(self) -> int:
        try:
            return self.qu[-1]
        except:
            return -1

    def isEmpty(self) -> bool:
        if len(self.qu)==0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if len(self.qu)==self.size:
            return True
        else:
            return False
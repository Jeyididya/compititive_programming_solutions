class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head=ListNode()
        self.count=0
        
    def get(self, index: int) -> int:
        x=self.head
        try:
            while x.next:
                print(x.val)
                x=x.next
            print(x.val)
            print("--")
            if not self.head:
                return null
            i=self.head
            try:
                for y in range(index):
                    i=i.next
                return i.val
            except:
                return -1
        except:
            return -1
    def addAtHead(self, val: int) -> None:
        if self.head.val ==-1:
            self.head.val =val
        else:
            temp=ListNode(val)
            temp.next=self.head
            self.head=temp
        self.count+=1

    def addAtTail(self, val: int) -> None:
        if self.head.val ==-1:
            self.head=ListNode(val)
        else:
            i=self.head
            while i.next:
                i=i.next
            i.next=ListNode(val)
            self.count+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
        else:
            try:
                i=self.head
                for y in range(index-1):
                    i=i.next
                temp=ListNode(val)
                temp.next=i.next
                i.next=temp
            except:
                self.addAtTail(val)
        self.count+=1

        

    def deleteAtIndex(self, index: int) -> None:
        if index<=self.count:
            if index==0:
                self.head=self.head.next
            else:
                i=self.head
                for y in range(index-1):
                    i=i.next
                try:    
                    i.next=i.next.next
                except:
                    i.next=None
            self.count-=1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
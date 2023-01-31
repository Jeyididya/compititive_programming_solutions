# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sord=[]
        i=list1
        try:
            while i.next:
                sord.append(i.val)
                i=i.next
            
            sord.append(i.val)
        except:
            pass
        i=list2
        try:
            while i.next:
                sord.append(i.val)
                i=i.next
            
            sord.append(i.val)
        except:
            pass
        sord.sort()
        nu=1
        if len(sord)>0:
            newHead=ListNode(sord[0])
            ina=newHead
            for i in range(1,len(sord)):
                temp=ListNode(sord[i])
                ina.next=temp
                ina=ina.next
        else:
            return None
        return newHead
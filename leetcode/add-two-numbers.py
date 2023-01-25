# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num=[[],[]]
        while l1.next!=None:
            num[0].append(str(l1.val))
            l1=l1.next
        num[0].append(str(l1.val))
        while l2.next!=None:
            num[1].append(str(l2.val))
            l2=l2.next
        num[1].append(str(l2.val))
        num1="".join(num[0][::-1])
        num2="".join(num[1][::-1])
        
        an=str(int(num1)+int(num2))[::-1]
        ans=ListNode(int(an[0]))
        ioi=ans
        for i in an[1:]:
            la=ListNode(int(i))
            ioi.next=la
            ioi=ioi.next
        return ans
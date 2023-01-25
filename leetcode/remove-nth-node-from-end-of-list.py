# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count=1
        h=head
        while h.next:
            h=h.next
            count+=1
        nth=count-n
        if nth==0:
            head=head.next
            return head
        curr=head
        prev=None
        while nth>0:
            prev=curr
            curr=curr.next
            nth-=1
        prev.next=curr.next
        return head